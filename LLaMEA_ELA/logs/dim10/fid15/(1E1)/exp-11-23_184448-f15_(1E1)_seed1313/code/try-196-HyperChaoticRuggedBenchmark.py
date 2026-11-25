import numpy as np

class HyperChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base hyper-radial term with memory effects
        r_squared = np.sum(x**2)
        memory_factor = np.exp(-0.05 * r_squared) * (1.0 + 0.1 * np.sin(r_squared))
        radial_term = memory_factor * (r_squared + 1e-8)
        
        # Memory-dependent chaotic saddle points
        saddle_term = 0.0
        for i in range(self.dim):
            delay_idx = (i + self.dim//4) % self.dim
            freq = 2.0 + 3.0 * np.sin(i * np.pi / (self.dim + 1))
            # Add memory interaction
            memory_interaction = np.cos(x[i] * freq) * np.sin(x[i] * freq) * np.cos(x[delay_idx] * 0.7)
            saddle_term += memory_interaction
        
        # Dynamic fractal coupling with time-varying exponents
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                # Fractal scaling with dynamic exponent
                fractal_exp = 0.3 + 0.7 * np.sin(np.log(dist + 1) * (i + j + 1))
                coupling_term += (x[i]**2 + x[j]**2) * np.exp(-dist**fractal_exp)
        
        # Adaptive chaotic local minima with dynamic centers and depths
        local_minima = 0.0
        for i in range(self.dim):
            center = 4.0 * np.sin(i * np.pi / (self.dim + 4)) * np.cos(i * np.pi / (self.dim + 6))
            depth = 1.5 + 0.8 * np.sin(i * np.pi / (self.dim + 3))
            # Adaptive width based on dimensionality
            width_factor = 1.0 + 0.2 * np.log(self.dim + 1)
            weight = np.exp(-0.2 * width_factor * (x[i] - center)**2)
            local_minima += weight * depth * (x[i]**5 - 2*x[i]**3 + x[i])**2
        
        # Multi-scale hyper-chaotic symmetry with dynamic delays
        symmetry_term = 0.0
        scales = [0.1, 0.4, 1.0, 2.0, 3.0]
        for scale in scales:
            delayed_r = np.sum(np.roll(x, self.dim//5)**2)
            # Dynamic phase modulation
            phase_mod = np.sin(r_squared / (scale + 0.5)) * np.cos(delayed_r / (scale + 1.5))
            symmetry_term += phase_mod
        
        # Adaptive noise with dynamic amplitude and frequency
        noise = 0.0
        for i in range(self.dim):
            amp = 0.8 + 0.4 * np.sin(i * np.pi / (self.dim + 2))
            freq = 1.5 + 2.5 * np.cos(i * np.pi / (self.dim + 3))
            noise += amp * np.sin(x[i] * freq) * np.cos(x[i] * (freq + 1)) * np.tan(x[i] / (i + 4))
        
        # Dimensionality-dependent hyper-scaling with dynamic exponent
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * np.pi / 3)
        
        return dim_factor * (0.2 * radial_term + 0.25 * saddle_term + 
                            0.2 * coupling_term + 0.2 * local_minima + 
                            0.1 * symmetry_term + 0.05 * noise)