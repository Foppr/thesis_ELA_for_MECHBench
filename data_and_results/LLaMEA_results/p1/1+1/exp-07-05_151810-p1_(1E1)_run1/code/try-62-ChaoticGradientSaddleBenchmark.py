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
        stiffness = 2.5 + 0.5 * np.sin(4.0 * x + np.pi/5)
        saddle = np.sum(stiffness * x**2 * np.cos(4.0 * x) * np.exp(-0.15 * x**2))
        
        # Multi-scale Gaussian peaks with altered chaotic positioning
        peaks = 0.0
        for i in range(self.dim):
            peak_pos = 2.5 * np.sin(1.2 * i + x[i]) + 1.8  # Slight shift in frequency and offset
            peak_height = 2.5 + 0.6 * np.cos(0.5 * i + 0.1)  # Slight shift in phase
            peaks += peak_height * np.exp(-0.5 * (x[i] - peak_pos)**2 / (0.4 + 0.3 * np.sin(i + 0.6)))  # Slight change in denominator
        
        # Enhanced gradient-influenced barrier with oscillating potential
        barrier = np.sum(1.2 / (1.0 + np.exp(2.5 * (x - 0.6 * np.sin(x)))))
        
        # Enhanced variable damping harmonic oscillator component with modified coefficients
        damping = 0.8 + 0.4 * np.cos(0.9 * x + np.pi/3)  # Slight change in damping
        oscillator = np.sum(0.7 * damping * x**2 + 0.4 * np.sin(2.0 * x) * np.cos(2.0 * x))
        
        # Enhanced coupled chaotic logistic maps with altered spatial interaction
        logistic = 0.0
        for i in range(self.dim):
            if i == 0:
                logistic += 3.8 * x[i] * (1.0 - x[i])  # Slight change in logistic parameter
            else:
                logistic += 3.8 * x[i] * (1.0 - x[i]) * np.sin(0.5 * x[i-1] + 0.4 * np.cos(x[i-1]))  # Slight change in coupling
        
        # Combine all components
        result = chaotic_quad + saddle + peaks + barrier + oscillator + logistic
        
        return result