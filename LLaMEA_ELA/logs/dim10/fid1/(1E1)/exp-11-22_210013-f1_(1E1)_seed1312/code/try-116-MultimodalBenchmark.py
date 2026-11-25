import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term with enhanced conditioning
        quadratic = 0.2 * np.sum(x**2) + 0.02 * np.random.rand()
        
        # Sinusoidal oscillations with increased frequency and phase shifts
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += 1.5 * np.sin(9 * x[i]) * np.exp(-0.15 * (x[i] - 1)**2)
            sinusoidal += 0.5 * np.cos(7 * x[i]) * np.sin(4 * x[(i + 1) % self.dim])
        
        # Additional multimodal term with stronger cross-interactions and higher-order terms
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 1.2 * np.sin(5 * x[i]) * np.cos(4 * x[(i + 1) % self.dim])
            multimodal += 0.4 * x[i] * x[(i + 1) % self.dim]
            multimodal += 0.2 * np.sin(3 * x[i]) * np.sin(3 * x[(i + 2) % self.dim])
            multimodal += 0.15 * x[i]**3 * np.cos(3 * x[(i + 3) % self.dim])
        
        # Add a non-separable global structure component with additional complexity
        global_structure = 0.0
        for i in range(self.dim):
            global_structure += (x[i] - 2)**5
            global_structure += 0.7 * np.sin(8 * x[i]) * np.cos(6 * x[(i + 1) % self.dim])
            global_structure += 0.5 * np.cos(5 * x[i]) * np.sin(9 * x[(i + 2) % self.dim])
        
        # Add a high-frequency noise component to increase landscape complexity
        noise = 0.0
        for i in range(self.dim):
            noise += 0.4 * np.sin(30 * x[i]) * np.cos(25 * x[(i + 1) % self.dim])
        
        # Improved fitness with better scaling and additional complexity
        return 1.0 * quadratic + 1.8 * sinusoidal + 2.2 * multimodal + 1.5 * global_structure + 1.0 * noise