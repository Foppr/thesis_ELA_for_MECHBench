import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Quadratic term for global minimum at origin
        quadratic = np.sum(x_norm**2)
        
        # Multiple nested sinusoidal terms with varying frequencies and amplitudes
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += (np.sin(5 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i]) * 
                          np.sin(7 * np.pi * x_norm[i]) * np.exp(-0.2 * (x_norm[i] - 0.1)**2))
        
        # Add a more complex multimodal component with fractal-like structure
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += (np.sin(12 * np.pi * x_norm[i]) * np.cos(8 * np.pi * x_norm[i]) * 
                          np.sin(4 * np.pi * x_norm[i]) * np.exp(-0.15 * x_norm[i]**2))
        
        # Higher order polynomial terms for additional landscape complexity
        cubic = np.sum(x_norm**3)
        quartic = np.sum(x_norm**4)
        quintic = np.sum(x_norm**5)
        
        # Add exponential decay terms to create more challenging landscape
        exp_decay = 0.0
        for i in range(self.dim):
            exp_decay += np.exp(-0.5 * (x_norm[i] - 0.3)**2) * np.sin(15 * np.pi * x_norm[i])
        
        # Combine all terms with carefully tuned weights
        return 3 * quadratic + 4 * sinusoidal + 2.5 * multimodal + 0.3 * cubic + 0.15 * quartic + 0.05 * quintic + 30 * exp_decay + 40 * np.exp(-0.4 * np.sum(x_norm**2))