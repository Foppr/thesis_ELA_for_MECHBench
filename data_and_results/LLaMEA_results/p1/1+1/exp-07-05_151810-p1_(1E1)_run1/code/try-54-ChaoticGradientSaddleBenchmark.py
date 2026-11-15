import numpy as np

class ChaoticGradientSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Highly multimodal chaotic sine-modulated quadratic component
        chaotic_quad = np.sum(0.5 * x**2 * (1.0 + 0.7 * np.sin(5.0 * x + np.pi/4) * np.cos(2.0 * x)))
        
        # Dynamic saddle point regions with variable stiffness and coupling
        stiffness = 3.0 + 0.6 * np.sin(4.0 * x + np.pi/5)
        saddle = np.sum(stiffness * x**2 * np.cos(4.0 * x) * np.exp(-0.3 * x**2) * np.sin(0.5 * x))
        
        # Nested Gaussian peaks with dynamic positioning and varying heights
        peaks = 0.0
        for i in range(self.dim):
            peak_pos = 4.0 * np.sin(1.1 * i + x[i]) + 3.0 * np.cos(0.7 * i)
            peak_height = 4.0 + 0.8 * np.cos(0.5 * i) * np.sin(0.3 * x[i])
            peaks += peak_height * np.exp(-0.5 * (x[i] - peak_pos)**2 / (0.3 + 0.1 * np.sin(i + 2)))
        
        # Extreme gradient-influenced barrier with hyperbolic potential
        barrier = np.sum(1.0 / (1.0 + np.exp(5.0 * (x - 0.8 * np.sin(x) * np.cos(x)))))
        
        # Variable damping harmonic oscillator with time-varying parameters
        damping = 1.0 + 0.5 * np.cos(0.9 * x + np.pi/3)
        oscillator = np.sum(0.8 * damping * x**2 + 0.7 * np.sin(2.0 * x) * np.cos(2.0 * x) * np.exp(-0.1 * x**2))
        
        # Complex coupled chaotic logistic maps with memory effects and spatial interference
        logistic = 0.0
        for i in range(self.dim):
            if i == 0:
                logistic += 4.0 * x[i] * (1.0 - x[i]) * (1.0 + 0.2 * np.sin(x[i]))
            else:
                logistic += 4.0 * x[i] * (1.0 - x[i]) * (1.0 + 0.3 * np.sin(x[i-1] + 0.5 * np.cos(x[i-1]))) * np.cos(0.3 * x[i-1])
        
        # Add a high condition number component for numerical difficulty
        condition_component = np.sum(1000.0 * np.sin(0.1 * x)**2 * np.cos(0.05 * x)**2)
        
        # Combine all components
        result = chaotic_quad + saddle + peaks + barrier + oscillator + logistic + condition_component
        
        return result