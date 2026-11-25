import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term with noise
        quadratic = 0.1 * np.sum(x**2) + 0.02 * np.random.rand()
        
        # Sinusoidal oscillations with multiple local minima and phase shifts
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += np.sin(9 * x[i]) * np.exp(-0.15 * (x[i] - 1)**2)
            sinusoidal += 0.4 * np.cos(7 * x[i]) * np.sin(5 * x[(i + 1) % self.dim])
        
        # Additional multimodal term with stronger cross-interactions and higher-order terms
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.9 * np.sin(5 * x[i]) * np.cos(4 * x[(i + 1) % self.dim])
            multimodal += 0.3 * x[i] * x[(i + 1) % self.dim]
            multimodal += 0.15 * np.sin(3 * x[i]) * np.sin(3 * x[(i + 2) % self.dim])
            multimodal += 0.08 * x[i]**4 * np.cos(3 * x[(i + 3) % self.dim])
        
        # Add a non-separable global structure component with additional complexity
        global_structure = 0.0
        for i in range(self.dim):
            global_structure += (x[i] - 2)**5
            global_structure += 0.6 * np.sin(8 * x[i]) * np.cos(7 * x[(i + 1) % self.dim])
            global_structure += 0.4 * np.cos(6 * x[i]) * np.sin(9 * x[(i + 2) % self.dim])
        
        # Add a high-frequency noise component to increase landscape complexity
        noise = 0.0
        for i in range(self.dim):
            noise += 0.3 * np.sin(30 * x[i]) * np.cos(25 * x[(i + 1) % self.dim])
        
        # Improved fitness with better scaling and additional complexity
        return 1.0 * quadratic + 1.5 * sinusoidal + 2.0 * multimodal + 1.3 * global_structure + 0.8 * noise