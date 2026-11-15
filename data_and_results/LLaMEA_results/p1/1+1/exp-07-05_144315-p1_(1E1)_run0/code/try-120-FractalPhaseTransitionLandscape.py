import numpy as np

class FractalPhaseTransitionLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for fractal structure
        self.fractal_dims = np.arange(1, dim + 1)
        self.phase_shifts = np.linspace(0, 2*np.pi, dim, endpoint=False)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base fractal component with self-similarity
        fractal = 0.0
        for i in range(self.dim):
            # Multi-scale sinusoidal pattern with varying frequencies
            freq = 2 ** (i % 4 + 1)
            fractal += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) * np.exp(-0.1 * x[i]**2)
        
        # Phase transition component with dynamic thresholds
        phase = 0.0
        for i in range(self.dim):
            # Dynamic phase shift based on coordinate value
            phase_shift = self.phase_shifts[i] + 0.5 * np.sin(x[i] * 0.3)
            phase += np.sin(x[i] + phase_shift) * np.cos(x[i] * 0.5 + phase_shift) * np.exp(-0.05 * x[i]**2)
        
        # Multi-fractal structure with varying exponents
        multifrac = 0.0
        for i in range(self.dim):
            # Different fractional powers for each dimension
            power = 1.2 + 0.3 * np.sin(i * 0.5)
            multifrac += np.abs(x[i])**power * np.sin(3 * x[i]) * np.exp(-0.08 * x[i]**2)
        
        # Self-similar peaks with varying heights and widths
        peaks = 0.0
        for i in range(1, 6):
            # Geometric progression of peak locations and widths
            center = 2.0 * np.sin(i * 0.8)
            width = 0.5 + 0.2 * np.cos(i * 0.6)
            peaks += np.exp(-0.5 * ((x - center) / width)**2) * np.sin(4 * np.sum(x - center))
        
        # Dynamic interaction term with time-like evolution
        dynamic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Time-dependent interaction with oscillating strength
                time_factor = 1.0 + 0.3 * np.sin(0.5 * (x[i] + x[j]))
                dynamic_interaction += time_factor * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Oscillatory basin component with multiple local minima
        basin = 0.0
        for i in range(self.dim):
            # Multiple oscillation frequencies for each dimension
            freqs = [2, 4, 6, 8]
            for freq in freqs:
                basin += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3) * np.exp(-0.03 * x[i]**2)
        
        # Scale-invariant component with recursive structure
        scale_inv = 0.0
        for i in range(self.dim):
            # Recursive-like pattern with diminishing contributions
            scale_inv += np.sin(2**i * x[i]) * np.cos(2**(i+1) * x[i]) * np.exp(-0.02 * x[i]**2)
        
        # Combined landscape with carefully balanced components
        result = 0.7 * fractal + 0.5 * phase + 0.6 * multifrac + 0.4 * peaks + 0.3 * dynamic_interaction + 0.8 * basin + 0.2 * scale_inv
        
        # Add a global scaling term that depends on the number of dimensions
        global_scale = 1.0 + 0.1 * np.log(self.dim + 1)
        result *= global_scale
        
        return result