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
            sinusoidal += np.sin(3 * np.pi * x_norm[i]) * np.sin(7 * np.pi * x_norm[i]) * np.exp(-0.5 * (x_norm[i] - 0.2)**2)
        
        # Add a more complex multimodal component
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += np.sin(10 * np.pi * x_norm[i]) * np.cos(5 * np.pi * x_norm[i]) * np.exp(-0.1 * x_norm[i]**2)
        
        # Cubic and quartic terms for additional landscape complexity
        cubic = np.sum(x_norm**3)
        quartic = np.sum(x_norm**4)
        
        # Combine all terms with carefully tuned weights
        return 5 * quadratic + 3 * sinusoidal + 2 * multimodal + 0.5 * cubic + 0.1 * quartic + 50 * np.exp(-0.3 * np.sum(x_norm**2))