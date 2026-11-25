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
        well_depths = 2.5 + 1.2 * np.sin(np.arange(self.dim) * 0.6)
        well_widths = 1.2 + 0.3 * np.cos(np.arange(self.dim) * 0.4)
        
        for i in range(self.dim):
            # Chaotic angular modulation with dynamic frequency
            angle = np.arctan2(x[i], x[(i+1) % self.dim]) if self.dim > 1 else 0
            freq_mod = 1.0 + 0.4 * np.sin(i * 0.3 + r * 0.15)
            well_term = well_depths[i] * np.exp(-0.5 * ((x[i] - 2.5 * np.sin(freq_mod * angle)) / well_widths[i])**2)
            result += well_term
            
        # Multi-scale harmonic interference with dynamic frequencies
        for i in range(self.dim):
            scale = 3**(i % 3 + 1) * (1.0 + 0.15 * np.sin(i * 0.25))
            result += 1.0 * np.sin(scale * x[i]) * np.cos(scale * x[i] * 0.35) * (1 + 0.15 * np.sin(i * 0.45))
            
        # Adaptive radial symmetry breaking with chaotic modulation
        angle_mod = 0.0
        for i in range(self.dim):
            angle_mod += 0.25 * np.sin(i * np.pi / 3.5 + r * 0.12) * np.cos(x[i] * 0.45)
            
        # Add radial periodic component with adaptive frequency
        radial_freq = 2.5 + 0.6 * np.sin(self.dim * 0.25 + r * 0.06)
        result += 1.8 * np.sin(radial_freq * r) * np.cos(radial_freq * r * 0.25)
        
        # Enhanced logarithmic barrier penalties with chaotic positioning and adaptive heights
        barrier_positions = 4.5 * np.sin(np.arange(self.dim) * 0.65 + r * 0.12)
        # Slight mutation: altered barrier height modulation for increased difficulty
        barrier_heights = 2.2 + 0.9 * np.sin(np.arange(self.dim) * 0.35 + r * 0.25 + 0.6 * np.sin(r * 0.35))
        
        for i in range(self.dim):
            distance_to_barrier = np.abs(np.abs(x[i]) - np.abs(barrier_positions[i]))
            if distance_to_barrier < 1.0:
                result += barrier_heights[i] * np.log(1 + 8 * distance_to_barrier**2)
                
        # Cross-dimensional coupling with enhanced chaotic interaction terms
        for i in range(self.dim):
            coupling = 0.0
            # Slight mutation: modified coupling strength and frequency
            for j in range(min(i+2, self.dim)):
                if i != j:
                    coupling += (x[i]**2 + x[j]**2) * np.sin(0.6 * (x[i] - x[j])) * (1 + 0.15 * np.sin(i * j * 0.35 + 0.45 * np.cos(r * 0.12)))
            result += 0.3 * coupling
            
        # Asymmetric exponential penalty with dynamic scaling
        # Slight mutation: adjusted penalty scale factor
        penalty_scale = 1.2 + 0.7 * np.sin(self.dim * 0.25 + r * 0.12 + 0.35 * np.cos(r * 0.25))
        for i in range(self.dim):
            result += penalty_scale * np.exp(1.8 * abs(x[i]) / 5.0) * (1 + 0.15 * np.cos(x[i] * 2.5 + r * 0.06))
            
        # Additional chaotic harmonic interference
        chaos_factor = 0.12 * np.sin(r * 0.45 + 0.25 * np.cos(r * 0.35))
        for i in range(self.dim):
            result += 0.35 * np.sin(6.5 * x[i] + chaos_factor) * np.cos(3.5 * x[i] + chaos_factor)
            
        return result