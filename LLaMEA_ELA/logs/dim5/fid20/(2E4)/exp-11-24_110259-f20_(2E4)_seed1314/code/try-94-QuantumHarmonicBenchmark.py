import numpy as np

class QuantumHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum harmonic oscillator parameters
        self.omega = np.random.rand(dim) * 3 + 1  # Frequency parameters
        self.alpha = np.random.rand(dim) * 0.8 + 0.2  # Coupling strengths
        self.beta = np.random.rand(dim) * 0.5 + 0.1  # Anharmonicity parameters
        self.gamma = np.random.rand(dim, dim) * 0.6 + 0.2  # Entanglement coefficients
        
    def f(self, x):
        # Scale input to [-pi, pi] for quantum harmonic functions
        x_scaled = x * (np.pi / 5.0)
        
        # Quantum harmonic oscillator potential terms
        potential_terms = []
        for i in range(self.dim):
            omega_i = self.omega[i]
            alpha_i = self.alpha[i]
            beta_i = self.beta[i]
            
            # Basic quantum harmonic oscillator: V(x) = (1/2)*omega^2*x^2
            harmonic_term = 0.5 * omega_i**2 * x_scaled[i]**2
            
            # Anharmonic correction: V(x) = (1/2)*omega^2*x^2 + beta*x^4
            anharmonic_term = beta_i * x_scaled[i]**4
            
            # Coupling with other dimensions through entanglement
            coupling_term = 0.0
            for j in range(self.dim):
                if i != j:
                    gamma_ij = self.gamma[i, j]
                    coupling_term += gamma_ij * np.sin(x_scaled[i]) * np.sin(x_scaled[j])
            
            potential_terms.append(harmonic_term + anharmonic_term + alpha_i * coupling_term)
        
        # Quantum tunneling effects with periodic modulation
        tunneling_effects = []
        for i in range(self.dim):
            # Periodic modulation of tunneling probability with fractal-like pattern
            tunneling_prob = np.sin(2 * x_scaled[i]) * np.cos(3 * x_scaled[i])
            tunneling_prob += 0.3 * np.sin(5 * x_scaled[i]) * np.cos(7 * x_scaled[i])
            tunneling_effects.append(tunneling_prob)
        
        # Entangled energy wells with adaptive depth and fractal structure
        entanglement_energy = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive coupling strength based on position with fractal scaling
                coupling_strength = self.gamma[i, j] * (1 + 0.5 * np.sin(x_scaled[i] + x_scaled[j]))
                coupling_strength *= (1 + 0.3 * np.cos(2 * (x_scaled[i] - x_scaled[j])))
                entanglement_energy += coupling_strength * np.cos(x_scaled[i] - x_scaled[j])
        
        # Global quantum interference pattern with fractal components
        interference_pattern = np.sum(np.sin(x_scaled) * np.cos(2 * x_scaled))
        interference_pattern += 0.3 * np.sum(np.sin(3 * x_scaled) * np.cos(4 * x_scaled))
        interference_pattern += 0.1 * np.sum(np.sin(5 * x_scaled) * np.cos(6 * x_scaled))
        interference_pattern += 0.05 * np.sum(np.sin(7 * x_scaled) * np.cos(8 * x_scaled))
        
        # Fractal-like position-dependent quantum tunneling
        tunneling_factor = 1.0 + 0.2 * np.sin(np.sum(x_scaled**2))
        tunneling_factor *= (1.0 + 0.15 * np.cos(np.sum(x_scaled**3)))
        tunneling_factor *= (1.0 + 0.1 * np.sin(4 * np.sum(x_scaled)))
        
        # Combine all terms with adaptive weighting
        result = (np.sum(potential_terms) + 
                 0.8 * np.sum(tunneling_effects) + 
                 0.6 * entanglement_energy + 
                 0.4 * interference_pattern) * tunneling_factor
        
        # Add quantum noise with proper distribution and fractal characteristics
        noise = 0.001 * np.random.randn() * (1 + 0.1 * np.sin(np.sum(x_scaled)))
        noise += 0.0005 * np.random.randn() * np.cos(np.sum(x_scaled**2))
        noise += 0.0003 * np.random.randn() * np.sin(3 * np.sum(x_scaled))
        
        return result + noise