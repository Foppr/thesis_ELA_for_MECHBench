import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Multimodal component with exponential decay in correlations
        multimodal = 0
        for i in range(self.dim):
            # Create multiple local minima using sine waves with varying frequencies
            multimodal += np.sin(x_normalized[i] * 3.0)**2 + np.cos(x_normalized[i] * 2.0)**2
            
        # Periodic interaction terms with exponentially decaying weights
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Exponentially decaying correlation with periodic sine interaction
                weight = np.exp(-0.1 * (i + j))
                interaction += weight * np.sin(x_normalized[i] * x_normalized[j] * 1.5) * np.cos(x_normalized[i] + x_normalized[j])
        
        # Adaptive ruggedness controlled by dynamic scaling factor
        ruggedness = 0
        scaling_factor = 1.0 + 0.5 * np.sin(np.sum(x_normalized) * 0.5)
        for i in range(self.dim):
            # Add ruggedness with dynamic scaling
            ruggedness += np.abs(x_normalized[i])**1.7 * scaling_factor
            
        # Add a global sine-wave modulation to increase complexity
        global_modulation = np.sin(np.sum(x_normalized) * 0.8) * 0.5
        
        # Combine all components with different weights
        result = 0.4 * f1 + 0.3 * multimodal + 0.2 * interaction + 0.1 * ruggedness + global_modulation
        
        # Add small random perturbation to increase problem difficulty
        perturbation = 0.01 * np.sum(np.sin(x_normalized * 11) * np.cos(x_normalized * 9))
        result += perturbation
        
        return result