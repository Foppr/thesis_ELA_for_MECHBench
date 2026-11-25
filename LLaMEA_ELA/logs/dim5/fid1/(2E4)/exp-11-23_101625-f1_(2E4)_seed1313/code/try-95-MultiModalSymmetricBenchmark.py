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
        well_depths = 3.0 + 1.5 * np.sin(np.arange(self.dim) * 0.7)
        well_widths = 1.0 + 0.4 * np.cos(np.arange(self.dim) * 0.5)
        
        for i in range(self.dim):
            # Chaotic angular modulation with dynamic frequency
            angle = np.arctan2(x[i], x[(i+1) % self.dim]) if self.dim > 1 else 0
            freq_mod = 1.0 + 0.6 * np.sin(i * 0.4 + r * 0.2)
            well_term = well_depths[i] * np.exp(-0.5 * ((x[i] - 2.0 * np.sin(freq_mod * angle)) / well_widths[i])**2)
            result += well_term
            
        # Multi-scale harmonic interference with dynamic frequencies
        for i in range(self.dim):
            scale = 4**(i % 4 + 1) * (1.0 + 0.2 * np.sin(i * 0.3))
            result += 1.5 * np.sin(scale * x[i]) * np.cos(scale * x[i] * 0.4) * (1 + 0.2 * np.sin(i * 0.5))
            
        # Adaptive radial symmetry breaking with chaotic modulation
        angle_mod = 0.0
        for i in range(self.dim):
            angle_mod += 0.3 * np.sin(i * np.pi / 4.0 + r * 0.15) * np.cos(x[i] * 0.5)
            
        # Add radial periodic component with adaptive frequency
        radial_freq = 3.0 + 0.8 * np.sin(self.dim * 0.3 + r * 0.08)
        result += 2.0 * np.sin(radial_freq * r) * np.cos(radial_freq * r * 0.3)
        
        # Enhanced logarithmic barrier penalties with chaotic positioning and adaptive heights
        barrier_positions = 4.0 * np.sin(np.arange(self.dim) * 0.7 + r * 0.15)
        # Slight mutation: altered barrier height modulation for increased difficulty
        barrier_heights = 2.5 + 1.1 * np.sin(np.arange(self.dim) * 0.4 + r * 0.3 + 0.7 * np.sin(r * 0.4))
        
        for i in range(self.dim):
            distance_to_barrier = np.abs(np.abs(x[i]) - np.abs(barrier_positions[i]))
            if distance_to_barrier < 1.2:
                result += barrier_heights[i] * np.log(1 + 10 * distance_to_barrier**2)
                
        # Cross-dimensional coupling with enhanced chaotic interaction terms
        for i in range(self.dim):
            coupling = 0.0
            # Slight mutation: modified coupling strength and frequency
            for j in range(min(i+3, self.dim)):
                if i != j:
                    coupling += (x[i]**2 + x[j]**2) * np.sin(0.7 * (x[i] - x[j])) * (1 + 0.2 * np.sin(i * j * 0.4 + 0.5 * np.cos(r * 0.15)))
            result += 0.4 * coupling
            
        # Asymmetric exponential penalty with dynamic scaling
        # Slight mutation: adjusted penalty scale factor
        penalty_scale = 1.5 + 0.9 * np.sin(self.dim * 0.3 + r * 0.15 + 0.4 * np.cos(r * 0.3))
        for i in range(self.dim):
            result += penalty_scale * np.exp(2.0 * abs(x[i]) / 5.0) * (1 + 0.2 * np.cos(x[i] * 3.0 + r * 0.08))
            
        # Additional chaotic harmonic interference
        chaos_factor = 0.15 * np.sin(r * 0.5 + 0.3 * np.cos(r * 0.4))
        for i in range(self.dim):
            result += 0.4 * np.sin(7.0 * x[i] + chaos_factor) * np.cos(4.0 * x[i] + chaos_factor)
            
        # Add high-frequency noise component
        noise = 0.0
        for i in range(self.dim):
            noise += 0.3 * np.sin(20 * x[i] + 0.5 * r) * np.cos(15 * x[i] - 0.3 * r)
        result += noise
        
        # Add irregular ridge structures with time-varying harmonic interference
        ridge_strength = 0.8 + 0.4 * np.sin(r * 0.2)
        for i in range(self.dim):
            ridge_term = ridge_strength * np.exp(-0.5 * ((x[i] - 1.5 * np.sin(0.3 * r)) / 0.8)**2)
            result += ridge_term
            
        return result