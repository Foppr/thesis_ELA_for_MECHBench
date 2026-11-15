import numpy as np

class ChaoticGradientSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine-modulated quadratic component with dynamic frequency
        chaotic_quad = np.sum(0.6 * x**2 * (1.0 + 0.8 * np.sin(7.0 * x + np.pi/3)) * np.exp(-0.1 * x**2))
        
        # Enhanced saddle point regions with dynamic stiffness and coupled oscillation
        stiffness = 3.0 + 0.7 * np.sin(5.0 * x + np.pi/6)
        saddle = np.sum(stiffness * x**2 * np.cos(5.0 * x) * np.exp(-0.2 * x**2) * np.sin(0.5 * x))
        
        # Multi-scale Gaussian peaks with dynamic positioning and adaptive heights
        peaks = 0.0
        for i in range(self.dim):
            peak_pos = 3.0 * np.sin(1.3 * i + x[i]) + 2.0 * np.cos(0.7 * i)
            peak_height = 3.0 + 0.8 * np.cos(0.6 * i + 0.3 * x[i])
            peaks += peak_height * np.exp(-0.5 * (x[i] - peak_pos)**2 / (0.5 + 0.4 * np.sin(i + 0.7 * x[i])))
        
        # Enhanced gradient-influenced barrier with multi-frequency oscillation
        barrier = np.sum(1.5 / (1.0 + np.exp(3.0 * (x - 0.7 * np.sin(x) * np.cos(0.5 * x)))))
        
        # Enhanced variable damping harmonic oscillator component with phase coupling
        damping = 1.0 + 0.4 * np.cos(1.0 * x + np.pi/4) * np.sin(0.3 * x)
        oscillator = np.sum(0.8 * damping * x**2 + 0.5 * np.sin(3.0 * x) * np.cos(3.0 * x) * np.exp(-0.05 * x**2))
        
        # Enhanced coupled chaotic logistic maps with dynamic coupling strength and time delays
        logistic = 0.0
        for i in range(self.dim):
            if i == 0:
                logistic += 3.9 * x[i] * (1.0 - x[i])
            else:
                coupling_strength = 0.8 + 0.2 * np.sin(0.4 * i + x[i-1])
                logistic += 3.9 * x[i] * (1.0 - x[i]) * np.sin(coupling_strength * x[i-1] + 0.5 * np.cos(x[i-1]))
        
        # Additional chaotic modulation with time-varying parameters
        chaotic_mod = np.sum(0.3 * np.sin(8.0 * x + 0.5 * np.cos(2.0 * x)) * np.exp(-0.15 * x**2))
        
        # Combine all components with adaptive weighting
        result = chaotic_quad + saddle + peaks + barrier + oscillator + logistic + chaotic_mod
        
        return result