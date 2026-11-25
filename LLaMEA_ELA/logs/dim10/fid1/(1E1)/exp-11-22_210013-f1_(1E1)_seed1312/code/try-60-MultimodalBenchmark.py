import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term with chaotic noise
        quadratic = 0.1 * np.sum(x**2) + 0.05 * np.random.rand() * np.sin(100 * np.sum(x))
        
        # Nested sinusoidal oscillations with varying frequencies and phase shifts
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += np.sin(10 * x[i]) * np.exp(-0.05 * (x[i] - 1)**2)
            sinusoidal += 0.4 * np.cos(7 * x[i]) * np.sin(5 * x[(i + 1) % self.dim])
            sinusoidal += 0.2 * np.sin(3 * x[i]) * np.cos(8 * x[(i + 2) % self.dim])
            sinusoidal += 0.1 * np.cos(9 * x[i]) * np.sin(4 * x[(i + 3) % self.dim])
        
        # Complex multimodal term with nested cross-interactions and fractal-like behavior
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.8 * np.sin(5 * x[i]) * np.cos(4 * x[(i + 1) % self.dim])
            multimodal += 0.3 * x[i] * x[(i + 1) % self.dim]
            multimodal += 0.2 * np.sin(2 * x[i]) * np.sin(3 * x[(i + 2) % self.dim])
            multimodal += 0.15 * x[i]**3 * np.cos(3 * x[(i + 3) % self.dim])
            multimodal += 0.1 * np.sin(6 * x[i]) * np.cos(7 * x[(i + 4) % self.dim])
        
        # Global structure with chaotic and fractal characteristics
        global_structure = 0.0
        for i in range(self.dim):
            global_structure += (x[i] - 2)**4
            global_structure += 0.6 * np.sin(8 * x[i]) * np.cos(7 * x[(i + 1) % self.dim])
            global_structure += 0.4 * np.cos(5 * x[i]) * np.sin(9 * x[(i + 2) % self.dim])
            global_structure += 0.3 * np.sin(4 * x[i]) * np.cos(6 * x[(i + 3) % self.dim])
        
        # High-frequency chaotic noise component
        noise = 0.0
        for i in range(self.dim):
            noise += 0.3 * np.sin(50 * x[i]) * np.cos(40 * x[(i + 1) % self.dim])
            noise += 0.2 * np.cos(60 * x[i]) * np.sin(30 * x[(i + 2) % self.dim])
        
        # Fractal-like scaling component
        fractal = 0.0
        for i in range(self.dim):
            fractal += 0.15 * np.sin(15 * x[i]) * np.cos(12 * x[(i + 1) % self.dim])
            fractal += 0.1 * x[i]**4 * np.sin(8 * x[(i + 2) % self.dim])
        
        # Final fitness with enhanced complexity and chaotic scaling
        return 0.9 * quadratic + 1.5 * sinusoidal + 1.8 * multimodal + 1.3 * global_structure + 0.7 * noise + 0.5 * fractal