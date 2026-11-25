import numpy as np

class QuantumFractionalEntropyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute quantum harmonic oscillator frequencies
        self.frequencies = np.array([1.0 + 0.3 * np.sin(0.5 * np.pi * i) for i in range(dim)])
        # Precompute fractional calculus parameters
        self.frac_orders = np.array([0.3 + 0.4 * np.cos(0.4 * np.pi * i) for i in range(dim)])
        # Precompute topological entropy weights
        self.entropy_weights = np.array([0.5 + 0.5 * np.sin(0.6 * np.pi * i) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator term
        quantum_term = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i]
            quantum_term += 0.5 * freq * x[i]**2 + 0.25 * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        quantum_term /= self.dim
        
        # Fractional calculus based term with memory effects
        frac_term = 0.0
        for i in range(self.dim):
            order = self.frac_orders[i]
            # Approximate fractional derivative using finite differences
            frac_derivative = (x[i] ** (1 - order) * np.sin(x[i])) / (1 - order)
            frac_term += frac_derivative * np.exp(-0.05 * x[i]**2)
        frac_term /= self.dim
        
        # Topological entropy based coupling
        topo_term = 0.0
        for i in range(self.dim):
            weight = self.entropy_weights[i]
            topo_term += weight * (np.abs(x[i]) ** 1.5 + 0.3 * np.cos(2 * x[i])) * np.exp(-0.1 * x[i]**2)
        topo_term /= self.dim
        
        # Cross-dimensional interaction with quantum coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.4 + 0.3 * np.cos(0.3 * (x[i] + x[j]))
                cross_term += coupling * np.exp(-0.08 * (x[i]**2 + x[j]**2)) * np.sin(x[i] * x[j])
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Rugged landscape with fractal-like features
        rugged_term = 0.0
        for i in range(self.dim):
            rugged_term += (x[i]**6 - 15.0 * x[i]**4 + 75.0 * x[i]**2 - 125.0) * np.exp(-0.07 * x[i]**2)
        rugged_term /= self.dim
        
        # Non-smooth regularization with discontinuous components
        smooth_term = 0.0
        for i in range(self.dim):
            smooth_term += (np.abs(x[i])**1.3 + 0.5 * np.sin(3 * x[i]) + 0.2 * np.cos(5 * x[i])) * np.exp(-0.09 * x[i]**2)
        smooth_term /= self.dim
        
        # Combined function with dynamic scaling
        total = (quantum_term + 
                 frac_term + 
                 topo_term + 
                 cross_term + 
                 rugged_term + 
                 smooth_term)
        
        return total