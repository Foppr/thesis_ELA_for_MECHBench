import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Quadratic term for global minimum at origin
        quadratic = np.sum(x_norm**2)
        
        # Multiple sinusoidal terms with different frequencies and amplitudes
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += np.sin(5 * np.pi * x_norm[i]) * np.sin(9 * np.pi * x_norm[i]) * np.exp(-0.5 * (x_norm[i] - 0.3)**2)
        
        # Add a more complex multimodal component with chaotic interactions
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += np.sin(15 * np.pi * x_norm[i]) * np.cos(8 * np.pi * x_norm[i]) * np.exp(-0.2 * x_norm[i]**2)
        
        # Add a fractal-like component with nested structure
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(20 * np.pi * x_norm[i]) * np.sin(12 * np.pi * x_norm[i]) * np.exp(-0.1 * (x_norm[i] - 0.1)**2)
        
        # Cubic and quartic terms for additional landscape complexity
        cubic = np.sum(x_norm**3)
        quartic = np.sum(x_norm**4)
        
        # Combine all terms with carefully tuned weights
        return 3 * quadratic + 4 * sinusoidal + 2.5 * multimodal + 1.5 * fractal + 0.3 * cubic + 0.05 * quartic + 40 * np.exp(-0.2 * np.sum(x_norm**2))