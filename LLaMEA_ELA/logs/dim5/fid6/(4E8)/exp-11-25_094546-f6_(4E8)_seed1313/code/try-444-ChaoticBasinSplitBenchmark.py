import numpy as np

class ChaoticBasinSplitBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Base quadratic with chaotic curvature modulation
            base = 0.5 * xi**2 * (1.0 + 0.3 * np.sin(13 * xi + self.dim * 0.7 + i * 0.5))
            
            # Multi-scale harmonic interference with dynamic frequencies and amplitudes
            harmonic_sum = 0.0
            for k in range(1, 10):
                freq = k * (1.0 + 0.2 * np.sin(i * 0.4 + k * 0.3))
                amp = 1.0 / (k**1.5) * (1.0 + 0.1 * np.cos(i * 0.6 + k * 0.5))
                phase = k * 0.8 + 0.2 * np.sin(i * 0.3 + k * 0.4)
                harmonic_sum += amp * np.sin(freq * xi + phase) * np.cos(freq * xi + phase * 0.7)
            
            # Chaotic basin splitting with exponential weighting and fractal scaling
            basin_split = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    dist = np.abs(xi - x_norm[j])
                    weight = np.exp(-dist * (1.0 + 0.5 * np.sin(i * 0.6 + j * 0.4)))
                    influence = np.sin(7 * xi + 3 * x_norm[j] + i * 0.3 + j * 0.2) * weight
                    basin_split += influence
            
            # Fractal-dimensional coupling with dynamic scaling and chaotic phase shifts
            coupling_term = 0.0
            for j in range(self.dim):
                if i != j:
                    dist = np.abs(xi - x_norm[j])
                    scale = 1.0 + 0.4 * np.sin(i * 0.5 + j * 0.6 + self.dim * 0.3)
                    phase_shift = 0.3 * np.cos(i * 0.7 + j * 0.8)
                    coupling_term += (dist**scale) * np.sin(5 * xi + 4 * x_norm[j] + phase_shift)
            
            # Dynamic chaotic conditioning with multi-fractal modulation
            condition_factor = 1.0 + 0.6 * np.sin(self.dim * 0.8 + i * 0.6) * np.cos(xi * 4.0 + self.dim * 0.3)
            
            # Multi-scale fractal interference pattern with chaotic amplitude and frequency modulation
            interference = 0.0
            for k in range(1, 8):
                freq = k * (1.0 + 0.3 * np.sin(i * 0.5 + k * 0.4))
                amp = 1.0 / (k**2.0) * (1.0 + 0.2 * np.cos(i * 0.8 + k * 0.6))
                phase = k * 0.9 + 0.1 * np.sin(i * 0.4 + k * 0.3)
                interference += amp * np.sin(freq * xi + phase) * np.cos(freq * xi + phase * 0.5)
            
            # Enhanced chaotic coupling with adaptive weighting and phase modulation
            enhanced_coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    dist = np.abs(xi - x_norm[j])
                    adaptive_weight = 1.0 + 0.3 * np.sin(i * 0.7 + j * 0.5 + self.dim * 0.4)
                    phase_mod = 0.2 * np.cos(i * 0.6 + j * 0.8 + xi * 0.3)
                    enhanced_coupling += adaptive_weight * (dist**1.5) * np.sin(6 * xi + 5 * x_norm[j] + phase_mod)
            
            # Add all components
            result += condition_factor * (base + harmonic_sum + basin_split + coupling_term + interference + enhanced_coupling)
        
        # Global scaling with chaotic dimension modulation and multi-fractal correction
        global_scale = 1.0 + 0.5 * np.sin(np.log(self.dim + 2) * 3.0) + 0.4 * np.cos(self.dim * 0.6) * (1.0 + 0.1 * np.sin(self.dim * 0.4))
        
        # Add a small chaotic perturbation to improve conditioning and avoid degenerate cases
        chaos_perturb = 0.01 * np.sum(np.sin(x_norm * 7.0 + self.dim * 0.5)) * np.cos(np.sum(x_norm**2))
        
        return (global_scale * result / self.dim) + chaos_perturb