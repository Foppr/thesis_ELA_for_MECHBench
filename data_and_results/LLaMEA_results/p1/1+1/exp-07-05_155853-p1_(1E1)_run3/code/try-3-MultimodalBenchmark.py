import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with multiple local minima using combined trigonometric and exponential terms
        multimodal = 0
        for i in range(self.dim):
            multimodal += np.sin(5.0 * x[i]) * np.exp(-0.1 * x[i]**2) + 0.5 * np.sin(3.0 * x[i])
        
        # Additional quadratic terms with shifted centers to create a more complex landscape
        quadratic = 0.2 * np.sum((x - 2.0)**2)
        
        # Add a cross-term interaction to increase dimensionality complexity
        cross_term = 0.1 * np.sum(x[:-1] * x[1:])
        
        # Combine all components to create a challenging optimization landscape
        return sphere + multimodal + quadratic + cross_term