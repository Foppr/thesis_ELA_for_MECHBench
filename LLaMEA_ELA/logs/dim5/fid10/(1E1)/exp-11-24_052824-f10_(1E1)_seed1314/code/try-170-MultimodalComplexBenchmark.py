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
        for i in range(min(5, self.dim)):
            rbf_term += np.exp(-0.5 * ((x - centers[i]) / (0.5 + 0.5 * np.sin(i)))**2)
        
        # Coupling terms between dimensions with sinusoidal modulation
        coupling_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += np.sin(0.3 * x[i] * x[j]) * (1 + 0.2 * np.cos(x[i] + x[j]))
        
        # High-frequency oscillatory component
        oscillatory = np.sum(np.sin(15 * x) * np.cos(8 * x))
        
        # Saddle-like structure with exponential decay
        saddle_like = np.sum((x**2 - 1)**2 * np.exp(-0.1 * x**2))
        
        # Add noise-like perturbations to increase complexity
        noise = np.sum(0.1 * np.sin(20 * x) * np.cos(15 * x))
        
        # Combine all components with different weights
        return (0.4 * poly_term + 
                0.3 * trig_term + 
                0.2 * rbf_term + 
                0.15 * coupling_term + 
                0.1 * oscillatory + 
                0.25 * saddle_like + 
                0.05 * noise)