import numpy as np

class MultimodalGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute peak positions in each dimension
        self.peaks = np.random.uniform(-4.0, 4.0, (10, dim))
        
    def f(self, x):
        # Scale input to [-5, 5] range if needed
        x_scaled = np.clip(x, -5.0, 5.0)
        
        # Base multimodal component with Gaussian peaks
        result = 0.0
        for i in range(10):  # 10 Gaussian peaks
            peak = self.peaks[i]
            # Exponentially decaying amplitude based on peak index
            amplitude = np.exp(-0.1 * i)
            # Gaussian with varying width and position
            sigma = 0.5 + 0.3 * np.sin(i * 0.5)
            exponent = -np.sum(((x_scaled - peak) / sigma) ** 2) / 2
            result += amplitude * np.exp(exponent)
        
        # Sinusoidal modulation to increase landscape complexity
        sin_modulation = 0.0
        for i in range(self.dim):
            sin_modulation += np.sin(x_scaled[i] * (1.0 + 0.2 * np.cos(i * 0.3)))
            
        # Add interaction terms between dimensions
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Interaction strength decays with distance
                dist = np.abs(x_scaled[i] - x_scaled[j])
                interaction += np.exp(-dist) * np.sin(x_scaled[i] * x_scaled[j])
        
        # Combine components with different weights
        return 2.0 * result + 0.5 * sin_modulation + 0.3 * interaction