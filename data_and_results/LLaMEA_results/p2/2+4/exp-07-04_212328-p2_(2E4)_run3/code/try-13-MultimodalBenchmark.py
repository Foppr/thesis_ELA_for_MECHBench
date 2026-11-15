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
        
        # Add a more complex multimodal component
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += np.sin(12 * np.pi * x_norm[i]) * np.cos(6 * np.pi * x_norm[i]) * np.exp(-0.15 * x_norm[i]**2)
        
        # Cubic and quartic terms for additional landscape complexity
        cubic = np.sum(x_norm**3)
        quartic = np.sum(x_norm**4)
        
        # Shifted global minimum to (0.1, 0.1, ..., 0.1) to increase difficulty
        shift = 0.1
        shifted_term = np.sum((x_norm - shift)**2)
        
        # Combine all terms with carefully tuned weights
        return 4 * quadratic + 4 * sinusoidal + 3 * multimodal + 0.6 * cubic + 0.15 * quartic + 40 * np.exp(-0.25 * np.sum(x_norm**2)) + 2 * shifted_term