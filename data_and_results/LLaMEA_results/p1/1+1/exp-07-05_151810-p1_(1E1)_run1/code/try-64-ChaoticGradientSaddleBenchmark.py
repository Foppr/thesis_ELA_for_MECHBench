import numpy as np

class ChaoticGradientSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine-modulated quadratic component
        chaotic_quad = np.sum(0.4 * x**2 * (1.0 + 0.6 * np.sin(5.0 * x + np.pi/4)))
        
        # Enhanced saddle point regions with increased stiffness variability
        stiffness = 3.0 + 0.4 * np.sin(4.0 * x + np.pi/5)
        saddle = np.sum(stiffness * x**2 * np.cos(4.0 * x) * np.exp(-0.15 * x**2))
        
        # Multi-scale Gaussian peaks with enhanced chaotic positioning
        peaks = 0.0
        for i in range(self.dim):
            peak_pos = 2.8 * np.sin(1.2 * i + x[i]) + 1.8
            peak_height = 2.8 + 0.5 * np.cos(0.6 * i)
            peaks += peak_height * np.exp(-0.5 * (x[i] - peak_pos)**2 / (0.35 + 0.25 * np.sin(i + 0.6)))
        
        # Enhanced gradient-influenced barrier with oscillating potential
        barrier = np.sum(1.3 / (1.0 + np.exp(2.7 * (x - 0.7 * np.sin(x)))))
        
        # Enhanced variable damping harmonic oscillator component
        damping = 0.85 + 0.35 * np.cos(0.85 * x + np.pi/3)
        oscillator = np.sum(0.75 * damping * x**2 + 0.45 * np.sin(2.0 * x) * np.cos(2.0 * x))
        
        # Enhanced coupled chaotic logistic maps with spatial interaction
        logistic = 0.0
        for i in range(self.dim):
            if i == 0:
                logistic += 3.85 * x[i] * (1.0 - x[i])
            else:
                logistic += 3.85 * x[i] * (1.0 - x[i]) * np.sin(0.55 * x[i-1] + 0.35 * np.cos(x[i-1]))
        
        # Combine all components
        result = chaotic_quad + saddle + peaks + barrier + oscillator + logistic
        
        return result