import numpy as np

class SpectralChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize spectral parameters for each dimension
        self.frequencies = np.random.uniform(1.0, 5.0, dim)
        self.amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.phases = np.random.uniform(0.0, 2.0 * np.pi, dim)
        self.damping_factors = np.random.uniform(0.1, 0.9, dim)
        self.coupling_strengths = np.random.uniform(0.3, 1.5, dim)
        # Chaotic parameters
        self.chaotic_params = np.random.uniform(0.5, 2.0, dim)
        self.spectral_orders = np.random.randint(2, 6, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add periodic spectral components with varying frequencies and amplitudes
        for i in range(self.dim):
            xi = x[i]
            freq = self.frequencies[i]
            amp = self.amplitudes[i]
            phase = self.phases[i]
            damping = self.damping_factors[i]
            
            # Periodic component with amplitude modulation
            periodic_term = amp * np.sin(freq * xi + phase) * np.exp(-damping * xi**2)
            result += periodic_term
            
        # Add spectral coupling between dimensions
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                coupling_strength = self.coupling_strengths[i] * self.coupling_strengths[j]
                
                # Spectral coupling with frequency interaction
                spectral_coupling = coupling_strength * np.sin(self.frequencies[i] * xi + self.frequencies[j] * xj)
                result += spectral_coupling
                
        # Add chaotic perturbation using sine-circle map
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_param = self.chaotic_params[i]
            order = self.spectral_orders[i]
            
            # Chaotic modulation with periodic forcing
            chaotic_term = np.sin(chaotic_param * xi + np.sin(order * xi))
            chaotic_perturbation += chaotic_term
            
        result += 0.2 * chaotic_perturbation
        
        # Add multi-modal ridge structure with spectral harmonics
        for i in range(self.dim):
            xi = x[i]
            amp = self.amplitudes[i]
            freq = self.frequencies[i]
            
            # Multi-modal component with harmonic frequencies
            modal_component = amp * (np.sin(freq * xi) + 0.5 * np.sin(2 * freq * xi) + 0.3 * np.sin(3 * freq * xi))
            result += modal_component
            
        # Add global scaling with spectral envelope
        spectral_envelope = 1.0 + 0.2 * np.sum(np.cos(self.frequencies * x))
        result *= spectral_envelope
        
        # Add dimensionally varying damping effects
        damping_effect = 0.0
        for i in range(self.dim):
            xi = x[i]
            damping = self.damping_factors[i]
            damping_effect += damping * np.exp(-0.5 * xi**2)
        result += 0.1 * damping_effect
        
        return result