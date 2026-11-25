import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term with chaotic noise
        quadratic = 0.1 * np.sum(x**2) + 0.02 * np.random.rand() * np.sin(100 * np.sum(x))
        
        # Sinusoidal oscillations with multiple local minima and phase shifts
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += np.sin(7 * x[i]) * np.exp(-0.1 * (x[i] - 1)**2)
            sinusoidal += 0.3 * np.cos(5 * x[i]) * np.sin(3 * x[(i + 1) % self.dim])
        
        # Additional multimodal term with stronger cross-interactions and higher-order terms
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.7 * np.sin(4 * x[i]) * np.cos(3 * x[(i + 1) % self.dim])
            multimodal += 0.25 * x[i] * x[(i + 1) % self.dim]
            multimodal += 0.1 * np.sin(2 * x[i]) * np.sin(2 * x[(i + 2) % self.dim])
            multimodal += 0.05 * x[i]**3 * np.cos(2 * x[(i + 3) % self.dim])
            # Add chaotic cross-term
            multimodal += 0.15 * np.sin(15 * x[i]) * np.cos(12 * x[(i + 1) % self.dim]) * np.sin(8 * x[(i + 2) % self.dim])
        
        # Add a non-separable global structure component with additional complexity
        global_structure = 0.0
        for i in range(self.dim):
            global_structure += (x[i] - 2)**4
            global_structure += 0.5 * np.sin(6 * x[i]) * np.cos(5 * x[(i + 1) % self.dim])
            global_structure += 0.35 * np.cos(4 * x[i]) * np.sin(7 * x[(i + 2) % self.dim])
            # Add chaotic component to global structure
            global_structure += 0.2 * np.sin(20 * x[i]) * np.cos(18 * x[(i + 1) % self.dim]) * np.sin(15 * x[(i + 2) % self.dim])
        
        # Add a high-frequency noise component to increase landscape complexity
        noise = 0.0
        for i in range(self.dim):
            noise += 0.35 * np.sin(25 * x[i]) * np.cos(20 * x[(i + 1) % self.dim])
            # Add chaotic noise term
            noise += 0.2 * np.sin(40 * x[i]) * np.cos(35 * x[(i + 1) % self.dim]) * np.sin(30 * x[(i + 2) % self.dim])
        
        # Improved fitness with better scaling and additional complexity
        return 0.8 * quadratic + 1.3 * sinusoidal + 1.7 * multimodal + 1.1 * global_structure + 0.85 * noise