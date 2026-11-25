import numpy as np

class RadialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Cluster centers for radial basis functions
        self.cluster_centers = np.random.uniform(-5.0, 5.0, (dim, 5))
        # Radial basis function widths
        self.rbf_widths = np.random.uniform(0.5, 2.0, 5)
        # Sinusoidal frequency modulation parameters
        self.freq_mod = np.random.uniform(1.0, 5.0, dim)
        # Path-dependent conditioning factors
        self.path_conditioning = np.random.uniform(0.5, 3.0, dim)
        # Amplitude scaling for sinusoidal components
        self.amp_scaling = np.random.uniform(0.5, 2.5, dim)
        # Phase shifts for sinusoidal components
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        # Local optimum positions
        self.local_optima = np.random.uniform(-5.0, 5.0, (dim, 3))
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial basis function component
        rbf_energy = 0.0
        for i in range(5):
            distance = np.sum((x - self.cluster_centers[:, i]) ** 2)
            rbf_energy += np.exp(-distance / (2 * self.rbf_widths[i] ** 2))
            
        # Sinusoidal modulation with frequency adaptation
        sin_energy = 0.0
        for i in range(self.dim):
            freq = self.freq_mod[i] * (1 + 0.3 * np.sin(x[i]))
            sin_energy += self.amp_scaling[i] * np.sin(freq * x[i] + self.phase_shifts[i])
            
        # Path-dependent conditioning
        path_energy = 0.0
        for i in range(self.dim):
            path_factor = self.path_conditioning[i] * (1 + 0.2 * np.cos(x[i]))
            path_energy += path_factor * x[i] ** 4
            
        # Local optima attraction
        local_energy = 0.0
        for i in range(self.dim):
            distances = np.abs(x[i] - self.local_optima[i, :])
            min_dist = np.min(distances)
            local_energy += min_dist ** 2
            
        # Combine all components
        total = 0.4 * rbf_energy + 0.35 * sin_energy + 0.2 * path_energy + 0.05 * local_energy
        
        return -total  # Negative because we want to minimize