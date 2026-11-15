import numpy as np

class ChaoticGradientSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-modulated quadratic component
        chaotic_quad = np.sum(0.5 * x**2 * (1.0 + 0.4 * np.sin(3.5 * x + np.pi/4)))
        
        # Embedded saddle point regions with variable stiffness (mutated)
        stiffness = 1.5 + 0.3 * np.sin(2.5 * x)
        saddle = np.sum(stiffness * x**2 * np.cos(2.5 * x) * np.exp(-0.15 * x**2))
        
        # Multi-scale Gaussian peaks with chaotic positioning (mutated)
        peaks = 0.0
        for i in range(self.dim):
            peak_pos = 2.5 * np.sin(0.8 * i + x[i]) + 1.5
            peak_height = 2.5 + 0.4 * np.cos(0.35 * i)
            peaks += peak_height * np.exp(-0.5 * (x[i] - peak_pos)**2 / (0.4 + 0.15 * np.sin(i)))
        
        # Gradient-influenced barrier with oscillating potential
        barrier = np.sum(1.0 / (1.0 + np.exp(2.5 * (x - 0.6 * np.sin(x)))))
        
        # Variable damping harmonic oscillator component (mutated)
        damping = 0.7 + 0.3 * np.cos(0.6 * x)
        oscillator = np.sum(0.5 * damping * x**2 + 0.4 * np.sin(1.6 * x) * np.cos(1.6 * x))
        
        # Coupled chaotic logistic maps with spatial interaction (mutated)
        logistic = 0.0
        for i in range(self.dim):
            if i == 0:
                logistic += 3.7 * x[i] * (1.0 - x[i])
            else:
                logistic += 3.7 * x[i] * (1.0 - x[i]) * np.sin(0.4 * x[i-1])
        
        # Combine all components
        result = chaotic_quad + saddle + peaks + barrier + oscillator + logistic
        
        return result