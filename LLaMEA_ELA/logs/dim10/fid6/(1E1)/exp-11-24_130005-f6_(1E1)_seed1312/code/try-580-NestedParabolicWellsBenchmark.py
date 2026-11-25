import numpy as np

class NestedParabolicWellsBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Nested parabolic wells with varying depths and radii
        well_energy = 0.0
        for i in range(self.dim):
            # Create nested wells with exponentially increasing depth
            radius = 0.5 + 0.3 * np.sin(i * 0.7)
            depth = 2.0 * (1.5 ** i)  # Exponentially increasing depths
            well_energy += depth * (x_scaled[i]**2 - radius**2)**2
        
        # Radial symmetry component with logarithmic barriers
        radial_energy = 0.0
        r_squared = np.sum(x_scaled**2)
        if r_squared > 1e-10:  # Avoid log(0)
            radial_energy = 1.5 * np.log(r_squared + 1e-10) * np.exp(-r_squared/2.0)
        
        # Cross-dimensional coupling with sinusoidal interactions
        coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Sinusoidal coupling with varying frequencies and amplitudes
                freq_i = 2.0 + 0.5 * np.sin(i * 0.3)
                freq_j = 1.5 + 0.4 * np.cos(j * 0.4)
                coupling_energy += np.sin(freq_i * x_scaled[i]) * np.cos(freq_j * x_scaled[j])
        
        # Logarithmic barrier regions near boundaries
        barrier_energy = 0.0
        for i in range(self.dim):
            # Create logarithmic barriers at -1 and 1
            barrier_energy += 2.0 * (np.log(1.0 + np.exp(-5.0 * (x_scaled[i] - 1.0))) + 
                                   np.log(1.0 + np.exp(-5.0 * (-x_scaled[i] - 1.0))))
        
        # Additional chaotic modulation with polynomial terms
        chaotic_energy = 0.0
        for i in range(self.dim):
            chaotic_energy += (x_scaled[i]**3 + 0.5 * x_scaled[i]**2 + 0.1 * x_scaled[i]) * \
                             np.sin(3.0 * x_scaled[i]) * np.exp(-0.5 * x_scaled[i]**2)
        
        # Combine all components with carefully tuned weights
        return 1.2 * well_energy + 0.8 * radial_energy + 1.5 * coupling_energy + 1.0 * barrier_energy + 0.7 * chaotic_energy