import numpy as np

class MultimodalComplexBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with mixed degrees
        poly_component = np.sum(x**4 + 0.5 * x**3 + 2 * x**2 + 0.1 * x)
        
        # Trigonometric oscillations with varying frequencies and amplitudes
        trig_component = 0
        for i in range(self.dim):
            trig_component += (np.sin(5 * x[i]) * np.cos(3 * x[i]) + 
                              0.7 * np.sin(7 * x[i]) * np.cos(2 * x[i]) + 
                              0.3 * np.sin(11 * x[i]))
            
        # Radial basis function component with multiple centers
        rbf_component = 0
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(self.dim):
            if i < len(centers):
                rbf_component += np.exp(-0.5 * (x[i] - centers[i])**2) * np.sin(2 * x[i])
                
        # Coupling between dimensions with chaotic-like behavior
        coupling_component = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling_component += (np.sin(x[i] + x[j]) * np.cos(0.3 * x[i] * x[j]) * 
                                    np.exp(-0.1 * (x[i]**2 + x[j]**2)))
                
        # Saddle-like structure with exponential decay
        saddle_component = 0
        for i in range(self.dim):
            saddle_component += (x[i]**2 - 1)**2 * np.exp(-0.3 * x[i]**2)
            
        # High-frequency noise component to increase conditioning difficulty
        noise_component = 0
        for i in range(self.dim):
            noise_component += 0.5 * np.sin(20 * x[i]) * np.cos(15 * x[i])
            
        # Combine all components with adaptive weights
        return (0.4 * poly_component + 
                0.3 * trig_component + 
                0.2 * rbf_component + 
                0.15 * coupling_component + 
                0.25 * saddle_component + 
                0.1 * noise_component + 
                3 * np.sum(np.abs(x)**0.5))