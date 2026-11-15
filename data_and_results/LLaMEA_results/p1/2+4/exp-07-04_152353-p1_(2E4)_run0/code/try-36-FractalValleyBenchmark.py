import numpy as np

class FractalValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Fractal component with self-similar structure
        fractal = 0
        for i in range(self.dim):
            # Create fractal-like behavior using multiple frequencies
            freq = 2**(i % 3 + 1)
            fractal += np.sin(x_normalized[i] * freq) * np.cos(x_normalized[i] * freq * 0.5)
            
        # Multi-scale valley structure with varying depths
        valley = 0
        for i in range(self.dim):
            # Create valleys at different scales
            scale = 2**(i % 4)
            valley += np.abs(x_normalized[i])**(1.2 + 0.3 * np.sin(i))
            
        # Gradient discontinuity component using step functions
        gradient_discontinuity = 0
        for i in range(self.dim):
            # Create discontinuous gradients with varying step sizes
            step = 0.5 + 0.3 * np.sin(i * 0.7)
            if x_normalized[i] > step:
                gradient_discontinuity += (x_normalized[i] - step)**2
            else:
                gradient_discontinuity += (x_normalized[i] + step)**2
                
        # Multi-modal component with varying amplitudes
        multimodal = 0
        for i in range(self.dim):
            # Create multiple local minima with different strengths
            amp = 1.0 + 0.5 * np.sin(i * 0.3)
            multimodal += amp * np.sin(x_normalized[i] * 5) * np.cos(x_normalized[i] * 3)
            
        # Combine all components with different weights
        result = 0.3 * f1 + 0.25 * fractal + 0.2 * valley + 0.15 * gradient_discontinuity + 0.1 * multimodal
        
        # Add a small random perturbation to increase problem difficulty
        perturbation = 0.01 * np.sum(np.sin(x_normalized * 11) * np.cos(x_normalized * 9))
        result += perturbation
        
        return result