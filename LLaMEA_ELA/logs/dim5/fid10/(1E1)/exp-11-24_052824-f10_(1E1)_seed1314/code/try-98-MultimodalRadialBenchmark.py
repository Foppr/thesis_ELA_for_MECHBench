import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with mixed degrees
        poly_base = np.sum(x**4) + 0.5 * np.sum(x**6)
        
        # Radial basis function component with multiple centers
        rbf = 0
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(len(centers)):
            if i < self.dim:
                rbf += np.exp(-0.5 * ((x[i] - centers[i])**2) / 0.5**2)
                
        # Trigonometric component with varying frequencies
        trig = 0
        for i in range(self.dim):
            trig += np.sin(3 * x[i]) + 0.5 * np.cos(7 * x[i]) + 0.3 * np.sin(11 * x[i])
            
        # Coupling terms between dimensions with nonlinear interactions
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling += (x[i]**2 + x[j]**2) * np.sin(0.5 * x[i] * x[j])
                
        # Saddle-like behavior with exponential modulation
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**2 - 1)**2 * np.exp(-0.3 * x[i]**2)
            
        # High-frequency oscillatory component
        oscillatory = 0
        for i in range(self.dim):
            oscillatory += np.sin(15 * x[i]) * np.cos(8 * x[i]) + 0.7 * np.sin(22 * x[i])
            
        # Add noise-like perturbations to increase complexity
        noise = 0.1 * np.sum(np.sin(10 * x) * np.cos(5 * x))
        
        # Combine all components with carefully chosen weights
        return (0.4 * poly_base + 
                0.3 * rbf + 
                0.2 * trig + 
                0.15 * coupling + 
                0.25 * saddle + 
                0.3 * oscillatory + 
                0.05 * noise + 
                3 * np.sum(np.abs(x)**3))