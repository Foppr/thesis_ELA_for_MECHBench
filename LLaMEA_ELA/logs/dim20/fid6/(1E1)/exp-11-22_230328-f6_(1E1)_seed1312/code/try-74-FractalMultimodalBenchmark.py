import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for different scales
        self.scales = np.logspace(0, 2, 5)  # 5 scales from 1 to 100
        self.amplitudes = np.logspace(0, 3, 5)  # Amplitudes for each scale
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Initialize result
        result = 0.0
        
        # Apply multi-scale fractal structure
        for i, (scale, amp) in enumerate(zip(self.scales, self.amplitudes)):
            # Create fractal component with different frequencies and phases
            freq = 2 * np.pi * scale
            phase = i * np.pi / 4
            
            # Fractal pattern using sine and cosine combinations
            fractal_term = amp * (
                np.sin(freq * x_norm + phase) * 
                np.cos(freq * x_norm * 0.5 + phase * 0.5) *
                np.exp(-0.1 * scale * np.sum(x_norm**2))
            )
            
            # Add hierarchical structure with varying weights
            weight = 1.0 / (1.0 + 0.1 * scale)
            result += weight * np.sum(fractal_term**2)
        
        # Add cross-dimensional coupling with fractal-like interactions
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            # Self-similar coupling pattern
            coupling_strength = 0.5 + 0.3 * np.sin(np.pi * (i + 1) / self.dim)
            cross_coupling += coupling_strength * (
                np.sin(3 * np.pi * (x_norm[i] + x_norm[i+1])) *
                np.cos(2 * np.pi * (x_norm[i] - x_norm[i+1]))
            )
        
        # Add global modulation with chaotic-like behavior
        r = np.sqrt(np.sum(x_norm**2))
        global_mod = 0.3 * np.sin(15 * r) * np.cos(8 * r) * np.exp(-0.5 * r)
        
        # Combine all components with dynamic scaling
        total_scale = 1.0 + 0.2 * np.sin(5 * r)
        
        return total_scale * (result + cross_coupling + global_mod)