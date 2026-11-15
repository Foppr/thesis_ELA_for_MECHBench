import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with adaptive exponents
        poly = np.sum((x**2 + 0.1 * x**4 + 0.01 * x**6))
        
        # Sine-cosine trigonometric component with varying frequencies
        trig = np.sum(np.sin(2.0 * x) * np.cos(1.5 * x) + np.sin(0.5 * x) * np.cos(0.3 * x))
        
        # Gaussian radial basis with dynamic width and center
        rb = np.sum(np.exp(-0.1 * (x - 1.0)**2) + np.exp(-0.05 * (x + 1.0)**2))
        
        # Cross-dimensional interaction terms with varying coupling strengths
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                cross += (np.sin(x[i]) * np.cos(x[j]) * 
                         np.exp(-0.01 * (x[i] - x[j])**2) * 
                         (1 + 0.1 * np.sin(0.2 * (x[i] + x[j]))))
        
        # Adaptive conditioning component with dimension-dependent scaling
        cond = 0
        for i in range(self.dim):
            cond += (0.5 * (i + 1) * x[i]**2 + 0.1 * (i + 1)**2 * x[i]**4)
        
        # Additional multimodal harmonic component
        harmonic = np.sum(np.sin(3.0 * x) * np.cos(2.0 * x) * np.sin(0.5 * x))
        
        # Combine all components with optimized weights
        return (0.4 * poly + 
                0.3 * trig + 
                0.15 * rb + 
                0.1 * cross + 
                0.05 * cond + 
                0.05 * harmonic)