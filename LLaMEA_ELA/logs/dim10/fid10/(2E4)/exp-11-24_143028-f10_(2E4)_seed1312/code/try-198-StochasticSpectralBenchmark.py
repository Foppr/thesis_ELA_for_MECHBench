import numpy as np

class StochasticSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired parameters with adaptive coupling strengths
        self.q_params = np.random.rand(min(15, dim)) * 0.8 + 0.2
        self.genetic_ops = np.random.rand(min(10, dim)) * 0.6 + 0.3
        self.memory_factors = np.random.rand(min(8, dim)) * 0.4 + 0.1
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum interference component with adaptive phase modulation
        quantum_term = 0.0
        for i in range(self.dim):
            # Quantum harmonic oscillator with time-dependent frequency
            freq = 2 + 0.5 * np.sin(0.3 * x[i]) + 0.3 * np.cos(0.4 * x[i])
            phase = 0.1 * x[i]**2 + 0.2 * np.sin(x[i])
            quantum_term += (np.sin(freq * x[i] + phase)**2 + 
                           0.7 * np.cos(freq * x[i] + phase)**2) * \
                           (1 + 0.2 * np.sin(3 * x[i]) * np.cos(2 * x[i]))
        
        # Adaptive genetic algorithm-inspired landscape with memory effects
        genetic_term = 0.0
        for i in range(self.dim):
            # Memory-dependent fitness with chaotic evolution
            mem_val = self.memory_factors[i % len(self.memory_factors)]
            genetic_term += (x[i]**4 + 0.5 * np.sin(2 * x[i]) + 
                           0.3 * np.cos(3 * x[i])) * \
                           (1 + mem_val * np.sin(0.5 * x[i]))
        
        # Hyperchaotic system with multiple attractors and cross-dimensional coupling
        hyperchaos_term = 0.0
        for i in range(self.dim):
            # Multi-attractor chaotic dynamics with parameter switching
            chaos_val = (x[i]**3 - 1.5 * x[i] + 0.8 * np.sin(2 * x[i]) + 
                        0.2 * np.cos(3 * x[i]))**2
            hyperchaos_term += chaos_val + 0.4 * np.tan(0.6 * x[i])
        
        # Cross-dimensional interaction with quantum entanglement-inspired terms
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Limited coupling for complexity
                # Quantum-like entanglement with fractal modulation
                entangle = np.exp(-0.2 * (x[i] - x[j])**2) * \
                          np.sin(0.3 * (x[i] + x[j]))
                coupling_term += entangle * (x[i]**2 + x[j]**2)
        
        # Non-smooth component with quantum tunneling effects and adaptive penalties
        nonsmooth_term = 0.0
        for i in range(self.dim):
            # Piecewise function with quantum-like probability distributions
            if np.abs(x[i]) < 1:
                nonsmooth_term += (np.abs(x[i])**2.5 + 0.4 * np.sin(5 * x[i]))
            else:
                nonsmooth_term += (np.abs(x[i])**3.2 + 0.6 * np.cos(4 * x[i]) + 
                                 0.1 * np.tan(0.7 * x[i]))
        
        # Multi-scale quantum harmonic interference with adaptive amplitudes
        interference_term = 0.0
        for i in range(self.dim):
            for k in range(1, min(8, self.dim+1)):
                # Quantum harmonic oscillator with time-varying amplitude
                amp = 1 + 0.3 * np.sin(k * x[i]) * np.cos(i * 0.5)
                phase = 0.2 * x[i] + 0.1 * np.sin(0.4 * x[i])
                interference_term += amp * np.sin(k * x[i] + phase) * \
                                  np.cos(k**1.3 * x[i]) * \
                                  (1 + 0.15 * np.sin(2 * x[i]))
        
        # Boundary interaction with quantum tunneling and hyperchaotic penalties
        boundary_interaction = 0.0
        for i in range(self.dim):
            if x[i] < -4.8:
                # Quantum tunneling effect with exponential decay
                boundary_interaction += 3.5 * np.exp(-0.4 * (x[i] + 4.8)**2) * \
                                      np.sin(10 * x[i]) * np.cos(5 * x[i]) + \
                                      0.15 * np.tan(0.2 * x[i])
            elif x[i] > 4.8:
                # Hyperchaotic boundary effect with quantum-like oscillation
                boundary_interaction += 4.0 * np.exp(-0.3 * (x[i] - 4.8)**2) * \
                                      np.cos(9 * x[i]) * np.sin(4 * x[i]) + \
                                      0.1 * np.sin(0.6 * x[i])
        
        # Combine all components with optimized quantum-inspired weights
        result = 0.7 * quantum_term + 0.6 * genetic_term + 0.8 * hyperchaos_term + \
                 0.5 * coupling_term + 0.4 * nonsmooth_term + 0.6 * interference_term + \
                 0.35 * boundary_interaction
        
        return result