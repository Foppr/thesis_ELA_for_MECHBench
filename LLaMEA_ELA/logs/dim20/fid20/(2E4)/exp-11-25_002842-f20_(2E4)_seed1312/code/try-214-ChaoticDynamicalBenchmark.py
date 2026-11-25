import numpy as np

class ChaoticDynamicalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters
        self.num_oscillators = max(3, int(np.log2(dim)) + 2)
        self.chaos_parameters = np.random.uniform(0.1, 1.5, (self.num_oscillators, dim))
        self.fractional_orders = np.random.uniform(0.3, 0.9, (self.num_oscillators, dim))
        self.entanglement_strengths = np.random.uniform(0.5, 2.0, (self.num_oscillators, dim))
        self.noise_amplitudes = np.random.uniform(0.1, 0.8, (self.num_oscillators, dim))
        # Additional coupling and modulation parameters
        self.coupling_strengths = np.random.uniform(0.2, 1.2, (self.num_oscillators, self.num_oscillators))
        self.modulation_frequencies = np.random.uniform(0.5, 3.0, (self.num_oscillators, dim))
        self.modulation_amplitudes = np.random.uniform(0.3, 1.0, (self.num_oscillators, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quantum-inspired chaotic system with fractional-order dynamics
        result = 0.0
        for oscillator in range(self.num_oscillators):
            # Fractional-order chaotic dynamics
            chaotic_state = np.zeros(self.dim)
            for i in range(self.dim):
                # Fractional-order integration with chaos parameter
                frac_order = self.fractional_orders[oscillator, i]
                chaotic_state[i] = (
                    x_norm[i] * np.sin(self.chaos_parameters[oscillator, i] * x_norm[i]) + 
                    np.cos(self.chaos_parameters[oscillator, i] * x_norm[i]) *
                    np.exp(-0.5 * (x_norm[i] - 0.5)**2) * 
                    np.sin(2 * np.pi * x_norm[i])
                )
            
            # Entanglement coupling between oscillators
            entanglement_term = 0.0
            for other_osc in range(self.num_oscillators):
                if other_osc != oscillator:
                    coupling = self.coupling_strengths[oscillator, other_osc]
                    entanglement_term += coupling * np.sum(
                        np.sin(chaotic_state) * 
                        np.cos(self.entanglement_strengths[oscillator, :] * x_norm)
                    )
            
            # Adaptive noise modulation
            noise_modulation = 0.0
            for i in range(self.dim):
                noise_modulation += (
                    self.noise_amplitudes[oscillator, i] * 
                    np.sin(self.modulation_frequencies[oscillator, i] * x_norm[i]) *
                    np.cos(self.modulation_amplitudes[oscillator, i] * x_norm[i])
                )
            
            # Combine oscillator components
            oscillator_result = (
                np.sum(chaotic_state**2) + 
                entanglement_term + 
                noise_modulation * np.exp(-0.3 * np.sum(x_norm**2))
            )
            result += oscillator_result * np.exp(-0.2 * oscillator)
        
        # Multi-scale coupling terms with chaotic modulation
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling based on distance and modulation
                dist = np.abs(x_norm[i] - x_norm[j])
                chaos_mod = np.sin(dist * np.pi) * np.cos(2 * dist)
                coupling_terms += (
                    chaos_mod * 
                    np.exp(-dist**2 / (2 * (1.0 + 0.5 * np.sin(x_norm[i])))) *
                    np.sin(3 * (x_norm[i] - x_norm[j]))
                )
        
        # Additional chaotic harmonic components
        harmonic_component = 0.0
        for i in range(self.dim):
            harmonic_component += (
                0.9 * np.sin(2 * x_norm[i]) + 
                0.7 * np.cos(3 * x_norm[i]) + 
                0.5 * np.sin(5 * x_norm[i]) + 
                0.3 * np.cos(7 * x_norm[i]) +
                0.1 * np.sin(9 * x_norm[i])
            ) * np.exp(-0.4 * x_norm[i]**2)
        
        # Combine all components with chaotic scaling
        total = result * (1.0 + 0.3 * np.sin(np.sum(x_norm**2))) + \
                0.25 * coupling_terms + \
                0.15 * harmonic_component
        
        return total