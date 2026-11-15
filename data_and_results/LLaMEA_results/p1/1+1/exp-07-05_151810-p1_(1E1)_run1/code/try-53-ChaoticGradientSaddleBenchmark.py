import numpy as np

class ChaoticGradientSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine-modulated quadratic component
        chaotic_quad = np.sum(0.3 * x**2 * (1.0 + 0.5 * np.sin(4.0 * x + np.pi/3)))
        
        # Enhanced saddle point regions with increased stiffness variability
        stiffness = 2.0 + 0.4 * np.sin(3.0 * x + np.pi/6)
        saddle = np.sum(stiffness * x**2 * np.cos(3.0 * x) * np.exp(-0.2 * x**2))
        
        # Multi-scale Gaussian peaks with enhanced chaotic positioning
        peaks = 0.0
        for i in range(self.dim):
            peak_pos = 3.0 * np.sin(0.9 * i + x[i]) + 2.0
            peak_height = 3.0 + 0.5 * np.cos(0.4 * i)
            peaks += peak_height * np.exp(-0.5 * (x[i] - peak_pos)**2 / (0.5 + 0.2 * np.sin(i + 1)))
        
        # Enhanced gradient-influenced barrier with oscillating potential
        barrier = np.sum(1.0 / (1.0 + np.exp(3.0 * (x - 0.7 * np.sin(x)))))
        
        # Enhanced variable damping harmonic oscillator component
        damping = 0.8 + 0.4 * np.cos(0.7 * x + np.pi/4)
        oscillator = np.sum(0.6 * damping * x**2 + 0.5 * np.sin(1.8 * x) * np.cos(1.8 * x))
        
        # Enhanced coupled chaotic logistic maps with spatial interaction
        logistic = 0.0
        for i in range(self.dim):
            if i == 0:
                logistic += 3.8 * x[i] * (1.0 - x[i])
            else:
                logistic += 3.8 * x[i] * (1.0 - x[i]) * np.sin(0.5 * x[i-1] + 0.2 * np.cos(x[i-1]))
        
        # Combine all components
        result = chaotic_quad + saddle + peaks + barrier + oscillator + logistic
        
        return result