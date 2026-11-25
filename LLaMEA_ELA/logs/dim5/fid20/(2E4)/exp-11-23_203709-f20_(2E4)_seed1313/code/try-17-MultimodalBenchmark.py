import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with chaotic sine modulations and shifted local minima
        multimodal = 0
        for i in range(self.dim):
            shifted_x = x[i] - 1.5
            multimodal += (shifted_x**4 - 12 * shifted_x**2 + 3 * shifted_x) * np.sin(5 * shifted_x)
        
        # Radial barrier component with exponential decay
        radial_barrier = 0
        r = np.sqrt(np.sum(x**2))
        radial_barrier = 10 * np.exp(-0.1 * r**2) * np.cos(2 * r)
        
        # Enhanced interaction term with chaotic coupling and higher frequency
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.sqrt((x[i] - x[j])**2 + 1e-8)
                interaction += 0.5 * x[i] * x[j] * np.sin(5 * distance) * np.cos(3 * (x[i] + x[j]))
        
        # Add a complex cross-term interaction with multiple trigonometric components
        cross_term = 0
        for i in range(self.dim):
            cross_term += np.cos(0.7 * x[i])**4 + np.sin(0.3 * x[i])**3
        
        # Chaotic component with logistic map-like behavior
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(10 * x[i]) * np.exp(-0.5 * x[i]**2)
        
        # Combine all components with modified weights and add a global offset
        return 0.1 * sphere + 2.0 * multimodal + 0.4 * interaction + 0.3 * cross_term + 0.2 * radial_barrier + 0.15 * chaotic + 20 * self.dim