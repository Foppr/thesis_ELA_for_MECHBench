import numpy as np

class MultiModalSymmetricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base radial quadratic term
        r = np.sqrt(np.sum(x**2))
        result = 0.1 * r**2
        
        # Multiple periodic attractor wells with varying depths and widths
        well_depths = np.array([2.0, 1.5, 3.0, 1.0, 2.5])[:self.dim]
        well_widths = np.array([1.2, 0.8, 1.5, 0.6, 1.0])[:self.dim]
        
        for i in range(self.dim):
            # Create periodic wells with radial symmetry breaking
            angle = np.arctan2(x[i], x[(i+1) % self.dim]) if self.dim > 1 else 0
            well_term = well_depths[i] * np.exp(-0.5 * ((x[i] - 3 * np.sin(angle)) / well_widths[i])**2)
            result += well_term
            
        # Radial symmetry breaking with chaotic angular modulation
        angle_mod = 0.0
        for i in range(self.dim):
            angle_mod += 0.3 * np.sin(i * np.pi / 4 + r * 0.1) * np.cos(x[i] * 0.5)
            
        # Add radial periodic component with varying frequency
        radial_freq = 2 + 0.5 * np.sin(self.dim * 0.3)
        result += 1.5 * np.sin(radial_freq * r) * np.cos(radial_freq * r * 0.3)
        
        # Logarithmic barrier penalties near boundaries with chaotic positioning
        barrier_positions = 5 * np.sin(np.arange(self.dim) * 0.7)
        barrier_heights = 2.0 + 0.5 * np.sin(np.arange(self.dim) * 0.4)
        
        for i in range(self.dim):
            distance_to_barrier = np.abs(np.abs(x[i]) - np.abs(barrier_positions[i]))
            if distance_to_barrier < 1.0:
                result += barrier_heights[i] * np.log(1 + 10 * distance_to_barrier**2)
                
        # Cross-dimensional coupling with asymmetric interaction terms
        for i in range(self.dim):
            coupling = 0.0
            for j in range(min(i+2, self.dim)):
                if i != j:
                    coupling += (x[i]**2 + x[j]**2) * np.sin(0.5 * (x[i] - x[j]))
            result += 0.2 * coupling
            
        # Multi-scale harmonic interference patterns
        for i in range(self.dim):
            scale = 2**(i % 3 + 1)
            result += 0.8 * np.sin(scale * x[i]) * np.cos(scale * x[i] * 0.4) * (1 + 0.2 * np.sin(i * 0.5))
            
        # Asymmetric exponential penalty with chaotic scaling
        penalty_scale = 1.0 + 0.3 * np.sin(self.dim * 0.2)
        for i in range(self.dim):
            result += penalty_scale * np.exp(1.5 * abs(x[i]) / 5.0) * (1 + 0.1 * np.cos(x[i] * 3))
            
        return result