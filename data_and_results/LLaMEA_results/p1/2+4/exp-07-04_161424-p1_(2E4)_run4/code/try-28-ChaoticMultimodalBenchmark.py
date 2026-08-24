import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map sequence for chaos
        self.logistic_seq = np.array([0.5])
        for i in range(dim * 20):
            self.logistic_seq = np.append(self.logistic_seq, 4 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1]))
        self.logistic_seq = self.logistic_seq[:dim]
        
        # Precompute quantum-like phase factors
        self.phase_factors = np.exp(1j * np.random.uniform(0, 2*np.pi, dim))
    
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Radial basis function component with chaotic scaling
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            rbfs[i] = np.exp(-np.sum((x_norm - self.logistic_seq[i])**2) / (2 * 0.1**2))
        
        # Logistic map chaotic dynamics with quantum interference
        chaotic = np.sum(self.logistic_seq * np.sin(2 * np.pi * x_norm) * np.real(self.phase_factors))
        
        # Fractal noise component with dynamic scaling
        fractal_noise = np.sum(np.abs(x_norm)**(1.5 + np.sin(self.logistic_seq[0]) * 0.5) * np.random.uniform(0.1, 2.0, self.dim))
        
        # Quantum-like interference pattern
        interference = np.sum(np.abs(np.sin(x_norm * self.phase_factors)) * np.cos(x_norm * self.phase_factors))
        
        # Dynamic basin boundaries (non-smooth transitions)
        basin_boundaries = np.sum(np.abs(x_norm) * np.tanh(10 * x_norm))
        
        # Polynomial interaction with mixed degrees and chaotic coefficients
        poly_interaction = np.sum((x_norm**3) * (1 + 0.1 * self.logistic_seq)) + 0.5 * np.sum((x_norm**5) * (1 + 0.05 * self.logistic_seq)) + 0.1 * np.sum((x_norm**7) * (1 + 0.02 * self.logistic_seq))
        
        # Combine all components with varying weights
        return 0.25 * np.sum(rbfs) + 0.35 * chaotic + 0.2 * fractal_noise + 0.1 * interference + 0.05 * basin_boundaries + 0.05 * poly_interaction