import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Highly multimodal component with chaotic behavior
        multimodal = 0
        for i in range(self.dim):
            multimodal += (np.sin(x[i]) * np.cos(3 * x[i]) * 
                          np.exp(-((x[i] - np.pi)**2 / 5.0)) + 
                          0.5 * np.sin(2 * x[i]) * np.cos(4 * x[i]))
            
        # Additional complex harmonic component with multiple frequencies
        harmonic = 0
        for i in range(self.dim):
            harmonic += (np.sin(0.3 * x[i]) * np.cos(0.7 * x[i]) * 
                        np.exp(-((x[i] + np.pi)**2 / 15.0)) + 
                        0.3 * np.sin(1.5 * x[i]) * np.cos(2.5 * x[i]))
        
        # Add a chaotic component with exponential decay
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(x[i] * np.exp(-x[i]**2)) * np.cos(x[i] * np.exp(-x[i]**2))
            
        # Combine components with different weights and add a global scaling factor
        return (sphere * 0.1 + 
                multimodal * 0.4 + 
                harmonic * 0.3 + 
                chaotic * 0.2 + 
                0.1 * np.sin(np.sum(x**2) / 10.0))