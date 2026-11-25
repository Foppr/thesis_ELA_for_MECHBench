import numpy as np

class QuantumHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum harmonic oscillator parameters
        self.omega = np.random.uniform(0.5, 2.0, dim)
        self.mass = np.random.uniform(0.8, 1.5, dim)
        self.phase = np.random.uniform(0, 2*np.pi, dim)
        # Fractional Brownian motion parameters
        self.hurst = np.random.uniform(0.3, 0.8, dim)
        self.fractal_scale = np.random.uniform(0.5, 2.0, dim)
        # Adaptive coupling strengths
        self.coupling = np.random.uniform(0.1, 0.8, dim)
        # Basin conditioning parameters
        self.basin_center = np.random.uniform(-3.0, 3.0, dim)
        self.basin_width = np.random.uniform(0.5, 2.0, dim)
        self.entropy_weight = np.random.uniform(0.5, 1.5, dim)
        # Quantum tunneling and interference
        self.tunnel_prob = np.random.uniform(0.05, 0.3, dim)
        self.interference_amp = np.random.uniform(0.1, 0.5, dim)
        # Dynamic time-varying components
        self.time_factor = np.random.uniform(0.8, 1.2, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator energy
        quantum_energy = np.sum(0.5 * self.mass * self.omega**2 * x**2 + 0.5 * (np.gradient(x)**2) / self.mass)
        
        # Fractional Brownian motion terrain
        fbm_terrain = 0.0
        for i in range(self.dim):
            # Simplified fractional Brownian motion approximation
            fbm_terrain += self.fractal_scale[i] * np.sin(self.hurst[i] * x[i]) * np.cos(self.hurst[i] * x[i])
        
        # Adaptive coupling between dimensions
        coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_energy += self.coupling[i] * np.sin(x[i] - x[j]) * np.cos(x[i] - x[j])
        
        # Basin conditioning with entropy
        basin_attraction = 0.0
        for i in range(self.dim):
            distance = np.abs(x[i] - self.basin_center[i])
            basin_attraction += self.entropy_weight[i] * np.exp(-distance**2 / (2 * self.basin_width[i]**2))
        
        # Quantum tunneling effect
        tunneling = 0.0
        for i in range(self.dim):
            tunneling += self.tunnel_prob[i] * np.sin(x[i] + self.phase[i])
        
        # Interference pattern
        interference = 0.0
        for i in range(self.dim):
            interference += self.interference_amp[i] * np.cos(x[i] * self.omega[i] + self.phase[i])
        
        # Time-varying modulation
        time_mod = 0.0
        for i in range(self.dim):
            time_mod += self.time_factor[i] * np.sin(x[i] * self.omega[i])
        
        # Combine all components
        fitness = quantum_energy + fbm_terrain + coupling_energy + basin_attraction + tunneling + interference + time_mod
        
        # Normalize and add small noise
        fitness = fitness / self.dim
        noise = np.random.normal(0, 0.01)
        return fitness + noise