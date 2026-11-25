import numpy as np

class MultimodalComplexBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with mixed degrees
        poly_term = np.sum(x**4 + 0.5 * x**3 + 2 * x**2 + 0.1 * x)
        
        # Trigonometric component with multiple frequencies
        trig_term = np.sum(np.sin(2 * x) + 0.5 * np.sin(5 * x) + 0.3 * np.sin(10 * x))
        
        # Radial basis function component with varying centers and widths
        rbf_term = 0
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            width = 1.0 + 0.5 * np.sin(i)
            rbf_term += np.exp(-width * (x[i] - center)**2)
        
        # Coupling terms between dimensions with sinusoidal modulation
        coupling_term = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling_term += np.sin(0.5 * x[i]) * np.cos(0.3 * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # High-frequency oscillatory component
        high_freq = np.sum(np.sin(15 * x) + 0.7 * np.sin(25 * x) + 0.3 * np.sin(40 * x))
        
        # Saddle-like structure with exponential decay
        saddle_term = np.sum((x**2 - 1)**2 * np.exp(-0.5 * x**2))
        
        # Interaction terms creating complex landscape features
        interaction_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += (x[i]**2 + x[j]**2) * np.sin(0.2 * x[i] * x[j])
        
        # Final combined function with carefully balanced weights
        return (0.4 * poly_term + 
                0.3 * trig_term + 
                0.2 * rbf_term + 
                0.15 * coupling_term + 
                0.25 * high_freq + 
                0.3 * saddle_term + 
                0.2 * interaction_term + 
                3 * np.sum(np.cos(3 * x) + 0.5 * np.cos(7 * x)))