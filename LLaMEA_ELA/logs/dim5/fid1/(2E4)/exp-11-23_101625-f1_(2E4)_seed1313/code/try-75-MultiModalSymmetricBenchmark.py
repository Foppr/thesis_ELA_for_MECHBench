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
        well_depths = 2.0 + 1.5 * np.sin(np.arange(self.dim) * 0.7)
        well_widths = 1.0 + 0.5 * np.cos(np.arange(self.dim) * 0.5)
        
        for i in range(self.dim):
            # Chaotic angular modulation with dynamic frequency
            angle = np.arctan2(x[i], x[(i+1) % self.dim]) if self.dim > 1 else 0
            freq_mod = 1.0 + 0.3 * np.sin(i * 0.4 + r * 0.2)
            well_term = well_depths[i] * np.exp(-0.5 * ((x[i] - 3 * np.sin(freq_mod * angle)) / well_widths[i])**2)
            result += well_term
            
        # Multi-scale harmonic interference with dynamic frequencies
        for i in range(self.dim):
            scale = 2**(i % 4 + 1) * (1.0 + 0.2 * np.sin(i * 0.3))
            result += 0.8 * np.sin(scale * x[i]) * np.cos(scale * x[i] * 0.4) * (1 + 0.2 * np.sin(i * 0.5))
            
        # Adaptive radial symmetry breaking with chaotic modulation
        angle_mod = 0.0
        for i in range(self.dim):
            angle_mod += 0.3 * np.sin(i * np.pi / 4 + r * 0.1) * np.cos(x[i] * 0.5)
            
        # Add radial periodic component with adaptive frequency
        radial_freq = 2 + 0.5 * np.sin(self.dim * 0.3 + r * 0.05)
        result += 1.5 * np.sin(radial_freq * r) * np.cos(radial_freq * r * 0.3)
        
        # Enhanced logarithmic barrier penalties with chaotic positioning and adaptive heights
        barrier_positions = 5 * np.sin(np.arange(self.dim) * 0.7 + r * 0.1)
        barrier_heights = 2.0 + 0.8 * np.sin(np.arange(self.dim) * 0.4 + r * 0.2)
        
        for i in range(self.dim):
            distance_to_barrier = np.abs(np.abs(x[i]) - np.abs(barrier_positions[i]))
            if distance_to_barrier < 1.0:
                result += barrier_heights[i] * np.log(1 + 10 * distance_to_barrier**2)
                
        # Cross-dimensional coupling with enhanced chaotic interaction terms
        for i in range(self.dim):
            coupling = 0.0
            for j in range(min(i+3, self.dim)):
                if i != j:
                    coupling += (x[i]**2 + x[j]**2) * np.sin(0.5 * (x[i] - x[j])) * (1 + 0.1 * np.sin(i * j * 0.3))
            result += 0.2 * coupling
            
        # Asymmetric exponential penalty with dynamic scaling
        penalty_scale = 1.0 + 0.5 * np.sin(self.dim * 0.2 + r * 0.1)
        for i in range(self.dim):
            result += penalty_scale * np.exp(1.5 * abs(x[i]) / 5.0) * (1 + 0.1 * np.cos(x[i] * 3 + r * 0.05))
            
        # Additional chaotic harmonic interference
        chaos_factor = 0.1 * np.sin(r * 0.5)
        for i in range(self.dim):
            result += 0.3 * np.sin(7 * x[i] + chaos_factor) * np.cos(4 * x[i] + chaos_factor)
            
        return result