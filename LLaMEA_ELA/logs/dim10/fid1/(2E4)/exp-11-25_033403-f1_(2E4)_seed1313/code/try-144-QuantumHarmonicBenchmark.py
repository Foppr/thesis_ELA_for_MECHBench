import numpy as np

class QuantumHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize quantum harmonic oscillator parameters
        self.omega_params = np.random.uniform(0.5, 2.0, dim)
        self.coupling_strengths = np.random.uniform(0.1, 1.5, (dim, dim))
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        self.barrier_heights = np.random.uniform(1.0, 5.0, dim)
        # Add quantum tunneling probability
        self.tunnel_prob = np.random.uniform(0.01, 0.3, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator component
        quantum_term = 0.0
        for i in range(self.dim):
            # Harmonic potential with quantum corrections
            potential = 0.5 * self.omega_params[i]**2 * x[i]**2
            # Quantum kinetic energy correction (higher order terms)
            kinetic_correction = 0.1 * self.omega_params[i] * np.sin(x[i])
            quantum_term += potential + kinetic_correction
            
        # Phase interference patterns between dimensions
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Create complex phase relationships with tunable coupling
                coupling = self.coupling_strengths[i][j]
                phase_diff = np.abs(x[i] - x[j])
                interference_term += coupling * np.sin(phase_diff + self.phase_shifts[i] + self.phase_shifts[j])
                
        # Energy barrier modulation with quantum tunneling effects
        barrier_term = 0.0
        for i in range(self.dim):
            # Create multiple energy barriers with tunable heights
            barrier_height = self.barrier_heights[i]
            # Add quantum tunneling probability effect
            tunneling_effect = self.tunnel_prob[i] * np.exp(-0.5 * (x[i]**2) / (barrier_height**2))
            # Create barrier landscape with multiple peaks
            barrier_term += barrier_height * (1.0 + 0.5 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]))
            barrier_term += tunneling_effect
            
        # Non-separable cross-dimensional interactions
        cross_term = 0.0
        for i in range(self.dim):
            # Create highly non-linear coupling between all dimensions
            for j in range(self.dim):
                if i != j:
                    # Enhanced nonlinearity with polynomial and trigonometric combinations
                    dist = np.abs(x[i] - x[j])
                    cross_term += (self.coupling_strengths[i][j] * 
                                 np.sin(dist**2) * 
                                 np.cos(0.5 * x[i] * x[j]) * 
                                 np.exp(-0.1 * dist))
                    
        # Multi-scale quantum resonance patterns
        resonance_term = 0.0
        for i in range(self.dim):
            # Multiple quantum harmonic frequencies
            freqs = [1.0, 2.0, 3.0, 4.0, 5.0]
            resonance_sum = 0.0
            for freq in freqs:
                resonance_sum += np.sin(freq * x[i]) * np.cos(freq * x[i])
            resonance_term += resonance_sum
            
        # Add quantum fluctuation penalty near boundaries
        boundary_penalty = 0.0
        for i in range(self.dim):
            # Quantum uncertainty principle-inspired penalty
            penalty = 10.0 * (np.exp(-0.5 * (x[i] - 5.0)**2) + 
                            np.exp(-0.5 * (x[i] + 5.0)**2) + 
                            0.5 * np.sin(0.5 * x[i])**2)
            boundary_penalty += penalty
            
        # Combine all quantum components with modified weights
        total = 0.8 * quantum_term + 0.6 * interference_term + 0.7 * barrier_term + 0.9 * cross_term + 0.5 * resonance_term + 0.4 * boundary_penalty
        
        return total