import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Highly multimodal component with chaotic sine-wave interactions
        multimodal = 0
        for i in range(self.dim):
            multimodal += np.sin(10.0 * np.sin(2.0 * x[i])) * np.exp(-0.05 * x[i]**2) + \
                         0.7 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[i]) + \
                         0.3 * np.sin(7.0 * x[i])**3
        
        # Exponential decay barriers to create deep and narrow valleys
        barrier = 0
        for i in range(self.dim):
            barrier += 2.0 * np.exp(-0.5 * (x[i] - 1.0)**2) * np.exp(-0.3 * (x[i] + 1.0)**2)
        
        # Non-separable high-order polynomial terms
        polynomial = 0
        for i in range(self.dim - 1):
            polynomial += 0.5 * (x[i]**4 + x[i+1]**4) + 0.3 * x[i]**3 * x[i+1] + 0.2 * x[i] * x[i+1]**3
        
        # Add a chaotic cross-term interaction
        chaotic_cross = 0
        for i in range(self.dim - 2):
            chaotic_cross += np.sin(x[i] * x[i+1] * x[i+2]) * np.exp(-0.1 * (x[i]**2 + x[i+1]**2 + x[i+2]**2))
        
        # Combine all components to create a highly complex optimization landscape
        return sphere + multimodal + barrier + polynomial + chaotic_cross