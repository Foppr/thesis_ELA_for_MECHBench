import numpy as np

class MultiModalSymmetricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base radial quadratic term with adaptive scaling
        r = np.sqrt(np.sum(x**2))
        result = 0.1 * r**2
        
        # Enhanced periodic attractor wells with chaotic depth modulation
        well_depths = np.array([2.0, 1.5, 3.0, 1.0, 2.5, 1.8, 2.2, 1.3])[:self.dim]
        well_widths = np.array([1.2, 0.8, 1.5, 0.6, 1.0, 0.9, 1.1, 0.7])[:self.dim]
        
        for i in range(self.dim):
            # Chaotic angular modulation with adaptive frequency
            angle = np.arctan2(x[i], x[(i+1) % self.dim]) if self.dim > 1 else 0
            freq_mod = 1.0 + 0.3 * np.sin(i * 0.5 + r * 0.2)
            well_term = well_depths[i] * np.exp(-0.5 * ((x[i] - 3 * np.sin(freq_mod * angle)) / well_widths[i])**2)
            result += well_term
            
        # Enhanced radial symmetry breaking with multi-scale chaotic modulation
        angle_mod = 0.0
        for i in range(self.dim):
            angle_mod += 0.5 * np.sin(i * np.pi / 3 + r * 0.15) * np.cos(x[i] * 0.6)
            
        # Adaptive radial periodic component with dynamic frequency
        radial_freq = 2.5 + 0.8 * np.sin(self.dim * 0.4 + r * 0.1)
        result += 2.0 * np.sin(radial_freq * r) * np.cos(radial_freq * r * 0.25)
        
        # Adaptive logarithmic barrier penalties with dynamic positioning
        barrier_positions = 4.5 * np.sin(np.arange(self.dim) * 0.8 + r * 0.1)
        barrier_heights = 2.5 + 0.7 * np.sin(np.arange(self.dim) * 0.5 + r * 0.2)
        
        for i in range(self.dim):
            distance_to_barrier = np.abs(np.abs(x[i]) - np.abs(barrier_positions[i]))
            if distance_to_barrier < 1.2:
                result += barrier_heights[i] * np.log(1 + 15 * distance_to_barrier**2)
                
        # Enhanced cross-dimensional coupling with adaptive weights
        for i in range(self.dim):
            coupling = 0.0
            for j in range(min(i+3, self.dim)):
                if i != j:
                    weight = 0.3 * (1 + 0.2 * np.sin(i * 0.4 + j * 0.3))
                    coupling += weight * (x[i]**2 + x[j]**2) * np.sin(0.6 * (x[i] - x[j]))
            result += coupling
            
        # Multi-scale harmonic interference with dynamic scaling
        for i in range(self.dim):
            scale = 3**(i % 4 + 1)
            scale_mod = 1.0 + 0.25 * np.sin(i * 0.6 + r * 0.1)
            result += 1.0 * np.sin(scale_mod * scale * x[i]) * np.cos(scale_mod * scale * x[i] * 0.3) * (1 + 0.3 * np.sin(i * 0.4))
            
        # Enhanced asymmetric exponential penalty with dynamic scaling
        penalty_scale = 1.5 + 0.4 * np.sin(self.dim * 0.3 + r * 0.2)
        for i in range(self.dim):
            result += penalty_scale * np.exp(1.8 * abs(x[i]) / 5.0) * (1 + 0.15 * np.cos(x[i] * 3.5))
            
        # Additional chaotic noise term to improve conditioning
        noise = 0.1 * np.sum(np.sin(np.arange(self.dim) * 0.7 + r * 0.3) * x**2)
        result += noise
        
        return result