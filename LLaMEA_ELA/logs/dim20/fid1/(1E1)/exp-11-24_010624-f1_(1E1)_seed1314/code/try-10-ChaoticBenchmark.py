import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters using quaternion-like structure
        self.chaos_params = np.array([3.8 + 0.1 * np.sin(i * 1.2) for i in range(dim)])
        self.rotation_angles = np.array([i * np.pi / 4 + np.cos(i * 0.7) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Quaternion-inspired chaotic component with adaptive basins
        for i in range(self.dim):
            # Apply modified logistic map with quaternion-like rotation
            chaos_input = x[i] * np.cos(self.rotation_angles[i]) + x[(i+1) % self.dim] * np.sin(self.rotation_angles[i])
            chaotic_val = self.chaos_params[i] * chaos_input * (1 - chaos_input)
            
            # Adaptive basin structure with exponential scaling
            basin_scale = 1.0 + 0.5 * np.exp(-0.5 * x[i]**2)
            result += basin_scale * chaotic_val
            
        # High-dimensional trigonometric chaos with coupling
        for i in range(self.dim):
            # Multi-frequency trigonometric modulation
            trig_term = np.sin(2 * x[i]) + 0.5 * np.sin(5 * x[i]) + 0.3 * np.sin(8 * x[i])
            result += 0.8 * trig_term
            
        # Cross-dimensional coupling with complex interaction patterns
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Complex coupling with phase shift and distance-dependent strength
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                coupling = np.exp(-0.2 * dist) * np.sin(x[i] * x[j] + i * j * 0.1)
                result += coupling * (1 + 0.3 * np.cos(i - j))
                
        # Add global multimodal structure with multiple peaks
        global_peaks = 0.0
        for i in range(self.dim):
            # Multiple local peaks with varying heights and positions
            peak_height = 2.0 + 1.5 * np.sin(i)
            peak_pos = 2.0 * np.cos(i * 0.5) + 1.0
            global_peaks += peak_height * np.exp(-0.5 * (x[i] - peak_pos)**2)
            
        result += 0.5 * global_peaks
        
        # Add final chaotic modulation based on all dimensions
        sum_x = np.sum(x)
        result *= (1 + 0.3 * np.sin(sum_x) * np.cos(0.5 * sum_x))
        
        return result