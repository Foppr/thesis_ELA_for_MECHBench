import numpy as np

class ChaoticFractalInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize chaotic system parameters with modified ranges
        self.chebyshev_coeffs = np.random.uniform(-1.5, 1.5, (dim, 3))
        self.logistic_r = np.random.uniform(3.8, 4.0, dim)
        self.henon_a = np.random.uniform(1.3, 1.5, dim)
        self.henon_b = np.random.uniform(0.15, 0.35, dim)
        # Fractal structure parameters with increased complexity
        self.fractal_dims = np.random.uniform(1.2, 3.0, dim)
        self.fractal_scaling = np.random.uniform(0.05, 0.8, dim)
        # Quantum interference parameters with stronger coupling
        self.quantum_phases = np.random.uniform(0, 2*np.pi, (dim, dim))
        self.quantum_amplitudes = np.random.uniform(0.8, 2.5, (dim, dim))
        # Discontinuity and noise parameters with higher variability
        self.discontinuity_points = np.random.uniform(-5.0, 5.0, (dim, 7))
        self.noise_level = np.random.uniform(0.02, 0.15, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Chaotic dynamical systems (Chebyshev polynomials and logistic maps)
        for i in range(self.dim):
            # Chebyshev polynomial chaos
            cheb_val = self.chebyshev_coeffs[i][0] + self.chebyshev_coeffs[i][1] * x[i] + self.chebyshev_coeffs[i][2] * (2 * x[i]**2 - 1)
            result += np.abs(cheb_val)
            
            # Logistic map chaos
            logistic_val = x[i]
            for _ in range(7):
                logistic_val = self.logistic_r[i] * logistic_val * (1 - logistic_val)
            result += np.abs(logistic_val)
            
            # Hénon map chaos
            henon_x, henon_y = x[i], 0.0
            for _ in range(5):
                new_x = 1 - self.henon_a[i] * henon_x**2 + henon_y
                new_y = self.henon_b[i] * henon_x
                henon_x, henon_y = new_x, new_y
            result += np.abs(henon_x)
            
        # Fractal-like geometric structure
        for i in range(self.dim):
            fractal_term = 0.0
            for j in range(7):
                point = self.discontinuity_points[i][j]
                distance = np.abs(x[i] - point)
                fractal_term += (distance ** self.fractal_dims[i]) * self.fractal_scaling[i]
            result += fractal_term
            
        # Quantum interference patterns with additional cross-dimensional terms
        for i in range(self.dim):
            quantum_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    phase_diff = self.quantum_phases[i][j]
                    amplitude = self.quantum_amplitudes[i][j]
                    quantum_sum += amplitude * np.sin(x[i] * x[j] + phase_diff)
            result += 0.7 * quantum_sum**2
            
        # Add discontinuous noise terms with higher frequency
        for i in range(self.dim):
            noise_term = 0.0
            for j in range(5):
                if np.abs(x[i] - self.discontinuity_points[i][j]) < 0.15:
                    noise_term += self.noise_level[i] * np.random.uniform(-1, 1)
            result += noise_term
            
        # Add high-frequency oscillation to increase complexity
        for i in range(self.dim):
            result += 3.0 * np.sin(12 * x[i]) * np.cos(9 * x[i])
            
        # Add cross-dimensional coupling terms for increased difficulty
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i] - x[j])**4
        result += 0.5 * cross_term
        
        # Add a global scaling factor to control overall difficulty
        result *= (1.0 + 0.4 * np.sum(np.abs(x)))
        
        return result