import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with chaotic sine-wave interactions and quartic shaping
        multimodal = 0
        for i in range(self.dim):
            # Chaotic sine modulation with varying frequencies
            sine_term = np.sin(5 * np.pi * x[i]) * np.sin(7 * np.pi * x[i])
            # Quartic basin shaping with multiple local minima
            quartic_term = x[i]**4 - 10 * x[i]**2 + 5 * x[i]
            # Combined multimodal term
            multimodal += 0.5 * (quartic_term + 3 * sine_term * np.exp(-0.1 * x[i]**2))
        
        # Add strong cross-dimensional coupling with chaotic interactions
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic interaction term with exponential decay
                coupling = np.sin(np.pi * (x[i]**2 + x[j]**2)) * np.exp(-0.05 * (x[i] - x[j])**2)
                interaction += 0.3 * x[i] * x[j] * coupling
        
        # Add a global scaling factor and offset to increase conditioning difficulty
        return 0.05 * sphere + 1.5 * multimodal + 0.8 * interaction + 30 * self.dim