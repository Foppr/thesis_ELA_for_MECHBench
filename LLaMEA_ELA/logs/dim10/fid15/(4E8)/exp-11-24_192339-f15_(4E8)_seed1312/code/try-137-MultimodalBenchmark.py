import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component with dynamic frequency
        sin_component = 0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.3 * x[i])
            sin_component += np.sin(freq * x[i]) * np.cos(freq * x[i] / 3.0)
        
        # Radial basis function with dynamic width and multi-scale interactions
        rbf = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                dist = np.abs(x[i] - x[j])
                width = 0.5 + 0.5 * np.sin(0.2 * (x[i] + x[j]))
                rbf += np.exp(-0.5 * (dist / width)**2) * np.cos(2 * np.pi * dist)
        
        # Polynomial coupling with asymmetric interaction
        poly_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                term = (x[i]**2 + x[j]**2) * np.sin(0.4 * (x[i] - x[j]))
                poly_coupling += term * (1.0 + 0.3 * np.abs(x[i] - x[j]))
        
        # Dynamic conditioning with exponential scaling
        cond = 0
        for i in range(self.dim):
            cond += (1.0 + 0.5 * np.sin(0.6 * x[i])) * np.exp(0.1 * np.abs(x[i]))
        
        # Asymmetric noise component
        noise = 0.05 * np.sum(np.sin(7 * np.pi * x) ** 2 + 0.3 * np.cos(5 * np.pi * x) ** 2)
        
        # Global shift and scaling factor
        shift = 0.2 * np.sum(x**3)
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Combine all components with optimized weights
        return scale_factor * (0.5 * sin_component + 0.3 * rbf + 0.4 * poly_coupling + 
                              0.2 * cond) + shift + noise