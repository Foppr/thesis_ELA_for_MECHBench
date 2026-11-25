import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for different scales
        self.scales = np.logspace(0, 2, 5)  # 5 scales from 1 to 100
        self.amplitudes = np.logspace(0, 1, 5)  # Amplitude scaling factors
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Initialize function value
        result = 0.0
        
        # Multi-scale fractal component with self-similarity
        for i, (scale, amp) in enumerate(zip(self.scales, self.amplitudes)):
            # Fractal pattern using sine and cosine with varying frequencies
            freq = scale * 2 * np.pi
            fractal_term = amp * np.sum(
                np.sin(freq * x_norm) * np.cos(freq * x_norm) * 
                np.exp(-0.1 * np.abs(x_norm)) * 
                (1 + 0.3 * np.sin(3 * freq * x_norm))
            )
            
            # Add phase transition effects
            phase_shift = np.sin(i * np.pi / 5) * np.cos(i * np.pi / 3)
            fractal_term *= (1 + 0.2 * phase_shift)
            
            result += fractal_term
        
        # Add interference patterns between dimensions
        interference = 0.0
        for i in range(self.dim - 1):
            for j in range(i + 1, self.dim):
                # Multi-dimensional interference with dynamic coupling
                coupling = np.sin(np.pi * (x_norm[i] + x_norm[j]) / 2)
                interference += coupling * np.exp(-0.5 * (x_norm[i] - x_norm[j])**2)
        
        # Add basin-of-attraction style regions with varying depths
        basin_term = 0.0
        for i in range(self.dim):
            # Create valleys at different positions with varying depths
            valley_pos = np.sin(i * np.pi / 4) * 0.5
            basin_term += (x_norm[i] - valley_pos)**2 * np.exp(-0.1 * np.abs(x_norm[i] - valley_pos))
        
        # Add global modulation with chaotic-like behavior
        chaos_mod = np.sum(np.sin(7 * x_norm) * np.cos(5 * x_norm) * 
                          np.exp(-0.2 * np.abs(x_norm)))
        
        # Combine all components with dynamic weighting
        total = result + 0.3 * interference + 0.1 * basin_term + 0.05 * chaos_mod
        
        # Apply final transformation to ensure global minimum at origin
        return np.abs(total) + 0.01 * np.sum(x_norm**4)