import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial term with varying degrees and adaptive scaling
        poly_term = np.sum((x**3 + 0.5 * x**2.7 + 0.3 * x**1.8 + 0.1 * x**1.2) * (1 + 0.1 * np.abs(x)))
        
        # Trigonometric component with frequency modulation
        trig_term = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) + 
                          0.5 * np.sin(5 * np.pi * x) * np.cos(7 * np.pi * x))
        
        # Radial basis function with dynamic centers and widths
        rbf_term = 0.0
        centers = np.linspace(-4.5, 4.5, min(20, self.dim))
        widths = 0.5 + 0.3 * np.sin(np.arange(len(centers)) * np.pi / len(centers))
        
        for i, (center, width) in enumerate(zip(centers, widths)):
            if i < len(x):
                rbf_term += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Hybrid interaction term between adjacent variables
        hybrid_term = 0.0
        for i in range(self.dim - 1):
            hybrid_term += (x[i]**2 + x[i+1]**2) * np.sin(x[i] * x[i+1])
        
        # Asymmetric distortion using hyperbolic functions
        asym_term = np.sum(np.tanh(2 * x) + 0.3 * np.tanh(5 * x)**2)
        
        # Multi-scale oscillation component
        oscillation_term = np.sum(np.sin(10 * x) * np.cos(15 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Global scaling and offset to ensure positive fitness values
        return 0.25 * poly_term + 0.2 * trig_term + 0.15 * rbf_term + 0.12 * hybrid_term + 0.1 * asym_term + 0.08 * oscillation_term + 1.0