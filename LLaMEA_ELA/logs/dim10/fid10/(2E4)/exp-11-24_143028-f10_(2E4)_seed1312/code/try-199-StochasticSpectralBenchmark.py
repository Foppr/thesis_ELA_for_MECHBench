import numpy as np

class StochasticSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired superposition parameters
        self.q_params = np.random.rand(min(15, dim)) * 0.8 + 0.2
        self.genetic_weights = np.random.rand(min(15, dim)) * 3.0 + 1.0
        # Hyperchaotic system with multiple lyapunov exponents
        self.hyperchaos_params = np.random.rand(min(10, dim)) * 0.6 + 0.1
        self.fractal_dims = np.linspace(1.1, 2.9, min(15, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum superposition component with complex amplitude modulation
        quantum_term = 0.0
        for i in range(self.dim):
            # Quantum-like interference with phase rotation and fractal scaling
            phase = self.q_params[i] * x[i] + 0.3 * np.sin(x[i]**2)
            amp_mod = 1 + 0.5 * np.sin(i * 0.7) * np.cos(i * 0.4)
            quantum_term += amp_mod * (np.sin(phase)**2 + np.cos(phase)**2) * \
                           (1 + 0.3 * np.sin(2 * x[i]) * np.cos(3 * x[i]))
        
        # Genetic algorithm-inspired evolutionary landscape with adaptive crossover
        genetic_term = 0.0
        for i in range(self.dim):
            # Evolutionary mixing with dimensional scaling and fractal gene expression
            expr = self.genetic_weights[i] * (x[i]**2 + 0.5 * np.sin(3 * x[i]))
            genetic_term += expr * np.exp(-0.1 * x[i]**2) * \
                           (1 + 0.2 * np.cos(i * 0.5) * np.sin(i * 0.3))
        
        # Hyperchaotic dynamical system with multiple attractors
        hyperchaos_term = 0.0
        for i in range(self.dim):
            # Multiple lyapunov exponent dynamics with fractal basin boundaries
            chaos_val = self.hyperchaos_params[i] * x[i] * (1 - x[i]**2) + \
                       0.2 * x[i]**3 - 0.1 * np.sin(2 * x[i]) + \
                       0.05 * np.cos(3 * x[i]) * np.tan(0.5 * x[i])
            hyperchaos_term += chaos_val**5 + 0.7 * np.sin(4 * x[i]) + \
                              0.3 * np.cos(5 * x[i]) + 0.1 * np.tan(0.3 * x[i])
        
        # Fractal dimensionality scaling with multi-scale interaction
        fractal_term = 0.0
        for i in range(self.dim):
            # Dimensional scaling factor based on fractal dimensions
            scale_factor = self.fractal_dims[i] / (1 + np.exp(-0.5 * x[i]))
            fractal_term += (x[i]**2) * scale_factor + \
                           0.4 * np.sin(scale_factor * x[i]) * np.cos(scale_factor * x[i])
        
        # Cross-dimensional evolutionary coupling with genetic recombination
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Genetic interaction with chaotic mixing and adaptive weights
                weight_ij = 0.5 * (self.genetic_weights[i] + self.genetic_weights[j])
                coupling_term += weight_ij * np.sin(x[i] * x[j]) * \
                                np.exp(-0.2 * (x[i]**2 + x[j]**2)) + \
                                0.1 * np.cos(x[i] + x[j])**4
        
        # Adaptive penalty landscape with quantum tunneling effects
        penalty_term = 0.0
        for i in range(self.dim):
            # Quantum-like tunneling through boundaries with fractal potential wells
            if x[i] < -4.8:
                penalty_term += 3.0 * np.exp(-0.2 * (x[i] + 4.8)**2) * \
                               np.sin(15 * x[i]) * np.cos(7 * x[i]) + \
                               0.3 * np.tan(0.4 * x[i])
            elif x[i] > 4.8:
                penalty_term += 2.5 * np.exp(-0.3 * (x[i] - 4.8)**2) * \
                               np.cos(13 * x[i]) * np.sin(6 * x[i]) + \
                               0.2 * np.sin(0.6 * x[i])
        
        # Combine all components with quantum-inspired weighting scheme
        result = 0.9 * quantum_term + 0.7 * genetic_term + 0.8 * hyperchaos_term + \
                 0.6 * fractal_term + 0.5 * coupling_term + 0.4 * penalty_term
        
        return result