import numpy as np

class FractalOptimizationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term for global structure
        base = np.sum(x_normalized**2)
        
        # Fractal component using recursive sine-cosine patterns
        fractal = 0
        for i in range(self.dim):
            # Multi-scale fractal pattern with varying frequencies
            freq = 2**(i % 4 + 1)
            fractal += np.sin(freq * x_normalized[i]) * np.cos(freq * x_normalized[i])
            
        # Multi-scale gradient component with varying smoothness
        gradient = 0
        for i in range(self.dim):
            # Varying smoothness parameters for different dimensions
            smoothness = 0.5 + 0.5 * np.sin(i * 0.7)
            gradient += np.abs(x_normalized[i])**smoothness
            
        # Hybrid smooth/discontinuous regions
        hybrid = 0
        for i in range(self.dim):
            # Create regions that switch between smooth and discontinuous behavior
            if np.abs(x_normalized[i]) < 0.3:
                hybrid += x_normalized[i]**2
            else:
                hybrid += np.abs(x_normalized[i]) * np.sin(10 * x_normalized[i])
                
        # Self-similar structure with nested peaks and valleys
        nested = 0
        for i in range(self.dim):
            # Create nested structures with different scales
            scale = 2**(i % 3)
            nested += np.sin(scale * x_normalized[i]) * np.cos(scale * x_normalized[i])
            
        # Multi-scale noise component
        noise = 0
        for i in range(self.dim):
            # Add noise with varying amplitude and frequency
            amplitude = 0.1 + 0.05 * np.sin(i * 0.3)
            frequency = 5 + 3 * np.cos(i * 0.4)
            noise += amplitude * np.sin(frequency * x_normalized[i])
            
        # Combine all components with different weights
        result = 0.25 * base + 0.2 * fractal + 0.15 * gradient + 0.2 * hybrid + 0.15 * nested + 0.05 * noise
        
        # Add a small perturbation to increase problem difficulty
        perturbation = 0.01 * np.sum(np.sin(x_normalized * 13) * np.cos(x_normalized * 9))
        result += perturbation
        
        return result