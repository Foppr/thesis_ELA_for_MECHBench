import numpy as np

class QuantumFractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for stability
        self.fractal_dims = [0.3 + 0.4 * np.sin(i * np.pi / (self.dim + 1)) for i in range(self.dim)]
        self.oscillator_freqs = [1.0 + 0.5 * np.cos(i * np.pi / (self.dim + 2)) for i in range(self.dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator potential with varying frequencies
        quantum_potential = 0.0
        for i in range(self.dim):
            freq = self.oscillator_freqs[i]
            quantum_potential += 0.5 * freq**2 * x[i]**2 + 0.1 * np.sin(freq * x[i])
        
        # Fractional Brownian motion fractal component with varying Hurst parameters
        fractal_component = 0.0
        for i in range(self.dim):
            hurst = self.fractal_dims[i]
            # Simplified fractal approximation using power-law scaling
            scale_factor = np.abs(x[i])**hurst
            fractal_component += 2.0 * np.sin(scale_factor) * np.cos(2.0 * scale_factor)
        
        # Adaptive gating mechanism inspired by neural networks
        gating_sum = 0.0
        for i in range(self.dim):
            gate_input = x[i] * np.cos(i * np.pi / (self.dim + 1))
            gating_sum += 1.0 / (1.0 + np.exp(-gate_input))  # Sigmoid gating
        
        # Multi-scale interaction terms with chaotic modulation
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling with exponential decay
                coupling = np.exp(-0.3 * (x[i] - x[j])**2) * np.sin(3.0 * x[i] * x[j])
                interaction_term += coupling * (1.0 + 0.3 * np.sin(i + j))
        
        # Combine all components with adaptive weighting
        result = quantum_potential + fractal_component + 0.5 * gating_sum + interaction_term
        
        # Add a global periodic modulation to increase complexity
        period_mod = np.sin(0.5 * np.sum(x)) * np.cos(0.3 * np.sum(x**2))
        result += 0.8 * period_mod
        
        return result