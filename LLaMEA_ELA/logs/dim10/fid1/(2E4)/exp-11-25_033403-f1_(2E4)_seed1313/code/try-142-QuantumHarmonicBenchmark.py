import numpy as np

class QuantumHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize quantum harmonic oscillator parameters
        self.omega_params = np.random.uniform(0.5, 2.0, dim)
        self.coupling_strengths = np.random.uniform(0.1, 1.0, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        self.barrier_heights = np.random.uniform(1.0, 5.0, dim)
        self.energy_levels = np.random.randint(1, 6, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator component
        oscillator_term = 0.0
        for i in range(self.dim):
            omega = self.omega_params[i]
            energy_level = self.energy_levels[i]
            # Quantum harmonic potential with energy levels
            oscillator_term += 0.5 * omega**2 * x[i]**2 + 0.5 * energy_level
            
        # Phase interference component
        phase_term = 0.0
        for i in range(self.dim):
            phase = self.phase_shifts[i]
            # Create interference patterns using sine and cosine phases
            phase_term += np.sin(omega * x[i] + phase) * np.cos(omega * x[i] + phase)
            
        # Coupling interaction between dimensions
        coupling_term = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Tunable coupling strength with distance-based weighting
                    dist = np.abs(x[i] - x[j])
                    weight = self.coupling_strengths[i] * np.exp(-dist)
                    coupling_sum += weight * np.sin(x[i] + x[j])
            coupling_term += coupling_sum
            
        # Energy barrier modulation component
        barrier_term = 0.0
        for i in range(self.dim):
            height = self.barrier_heights[i]
            # Create modulated energy barriers using sigmoid functions
            barrier_term += height / (1.0 + np.exp(-x[i])) * (1.0 - 1.0 / (1.0 + np.exp(x[i])))
            
        # Multi-scale oscillatory structure with superposition
        multi_scale_term = 0.0
        scales = [1.0, 2.0, 3.0, 4.0]
        for scale in scales:
            scale_sum = 0.0
            for i in range(self.dim):
                scale_sum += np.sin(scale * x[i]) * np.cos(scale * x[i])
            multi_scale_term += scale_sum / len(scales)
            
        # Boundary modulation with quantum tunneling effect
        boundary_term = 0.0
        for i in range(self.dim):
            # Simulate quantum tunneling with exponential decay
            tunneling = np.exp(-0.1 * (x[i] - 5.0)**2) + np.exp(-0.1 * (x[i] + 5.0)**2)
            boundary_term += tunneling
            
        # Combine all components with adaptive weighting
        total = 0.3 * oscillator_term + 0.4 * phase_term + 0.5 * coupling_term + 0.6 * barrier_term + 0.2 * multi_scale_term + 0.3 * boundary_term
        
        return total